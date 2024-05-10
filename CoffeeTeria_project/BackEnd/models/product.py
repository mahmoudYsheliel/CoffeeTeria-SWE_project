from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id:Optional[str]
    name:str
    image:str
    description:str
    price:float