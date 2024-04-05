from pydantic import BaseModel
from typing import List

# base models

class UserBase(BaseModel):
    user: str
    # items: List[ItemBase]

class ItemBase(BaseModel):
    name: str
    description: str
    user_id: int