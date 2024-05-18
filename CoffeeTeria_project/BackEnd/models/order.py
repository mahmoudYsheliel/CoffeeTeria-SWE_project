from pydantic import BaseModel
from typing import Optional


class ItemCount(BaseModel):
    product_id:str
    count:int
    
class OrderInfo(BaseModel):
    location:Optional[str]=''
    time:Optional[str]=''
    number_of_seats:Optional[int]=0

class Order(BaseModel):
    id:Optional[str]=''
    coffee_shop_id:str
    customer_id:Optional[str]
    type:str #delivery pickup or book
    amount:Optional[float]=0
    created_at:str
    details:list[ItemCount]
    order_info:OrderInfo