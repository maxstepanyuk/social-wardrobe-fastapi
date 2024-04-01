from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the FastAPI instance
app = FastAPI()

# Database connection
# SQLALCHEMY_DATABASE_URL = "postgresql://fastapi_user:fastapi_user_password@127.0.0.1:5432/wardrobe_fastapi" # TODO
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/wardrobe_fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy Base
Base = declarative_base()

# Define your database models
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# Create the tables
Base.metadata.create_all(bind=engine)

user_list = [
    {"id": 1, "user":"adam"},
    {"id": 2, "user":"bill"},
    {"id": 3, "user":"kate"},
]

# FastAPI routes

@app.post("/items/")
def create_item(name: str, description: str):
    db = SessionLocal()
    item = Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/users")
async def list_users():
    # return {"message": "list users route"}
    return user_list

@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # return {"user_id": user_id}
    for user in user_list:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users")
async def create_user(user: dict):
    # Generate a new user ID
    new_user_id = max(user["id"] for user in user_list) + 1
    user["id"] = new_user_id
    user_list.append(user)
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: dict):
    for user in user_list:
        if user["id"] == user_id:
            user.update(updated_user)
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for index, user in enumerate(user_list):
        if user["id"] == user_id:
            del user_list[index]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
