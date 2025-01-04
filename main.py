from fastapi import FastAPI, HTTPException, Depends 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

app = FastAPI(
    title="Wardrobe FastAPI",
    description="by Maksym Stepanuik for Uni",
    version="0.0.1",
    docs_url="/docs"
) # Create the FastAPI instance

from database import engine, SessionLocal # from my files

import models # from my files
models.Base.metadata.create_all(bind=engine) # Create the tables


# get db then close the connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from typing import Annotated

db_dependency = Annotated[Session, Depends(get_db)] # dependency injection


# FastAPI routes

import schemas # from my files

def update_object_attributes(user_in, user): # TODO: move to a separate file?
    for attr, value in user_in.dict().items():
        setattr(user, attr, value)

@app.get("/")
async def root():
    return {"message":"hello world", "openapi swagger":"http://127.0.0.1:8000/docs"}

@app.post("/items/")
async def create_item(item_in: schemas.ItemBase, db: db_dependency):
    item = models.Item(**item_in.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/items")
async def list_items(db: db_dependency):
    item_list = db.query(models.Item).all()
    return item_list

@app.get("/items/{item_id}")
async def read_item(item_id: int, db: db_dependency):
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).one()
        return item
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Item not found")

@app.post("/users/")
async def create_user(user_in: schemas.UserBase, db: db_dependency):
    user = models.User(**user_in.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users")
async def list_users(db: db_dependency):
    user_list = db.query(models.User).all()
    return user_list

# @app.get("/users/me") # TODO
# async def get_current_user():
#     return {"Message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: db_dependency):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).one()
        return user
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
async def update_user(user_id: int, user_in: schemas.UserBase, db: db_dependency):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).one()
        update_object_attributes(user_in, user)
        db.commit()
        db.refresh(user)
        return user
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: db_dependency):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).one()
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
