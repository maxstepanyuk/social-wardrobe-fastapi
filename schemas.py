from pydantic import BaseModel
from typing import List, Optional

# base models

class UserBase(BaseModel):
    user: str
    # items: List[ItemBase]

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None  # Nullable string
    user_id: int