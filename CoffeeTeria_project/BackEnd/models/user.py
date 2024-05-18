from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id:Optional[str]=''
    username:str
    password:str
    balance:Optional[float]=0
    type:Optional[str]='Customer' #owner or customer
    city_name:Optional[str]='London'
    wish_list:Optional[list[str]] =[]
    
    
