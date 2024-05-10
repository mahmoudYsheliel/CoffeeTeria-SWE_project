from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ItemCount(BaseModel):
    product_id:str
    count:int

class Order(BaseModel):
    id:Optional[str]
    coffee_shop_id:str
    customer_id:Optional[str]
    created_at:datetime
    type:str #pickup or delivery
    amount:Optional[int]=0
    details:list[ItemCount]