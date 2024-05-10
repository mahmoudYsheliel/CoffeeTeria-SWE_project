from pydantic import BaseModel
from typing import Optional

class CoffeeShop(BaseModel):
    id:Optional[str]
    name:str
    city_name:str
    location:str
    open_time:int
    close_time:int
    image:str
    products:list[str]
    contact_number:str