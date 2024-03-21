from fastapi import FastAPI, HTTPException

app = FastAPI()

user_list = [
    {"id": 1, "user":"adam"},
    {"id": 2, "user":"bill"},
    {"id": 3, "user":"kate"},
]

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
