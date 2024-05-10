from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id:Optional[str]=''
    username:str
    password:str
    balance:Optional[int]=0
    type:str #owner customer
    city_name:str
    wish_list:Optional[list[str]] =[]
    
    
