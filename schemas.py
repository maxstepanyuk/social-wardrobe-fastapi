from pydantic import BaseModel, constr
from typing import List, Optional, Union

# base models

class UserBase(BaseModel):
    user: constr(min_length=1)

class ItemBase(BaseModel):
    name: constr(min_length=1)
    description: Optional[Union[constr(min_length=1), None]] = None
    user_id: Optional[int] = None