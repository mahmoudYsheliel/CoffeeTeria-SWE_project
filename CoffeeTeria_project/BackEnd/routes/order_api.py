from fastapi import APIRouter, Body,Depends
from models.order import Order
import database.order_database as order_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database


router = APIRouter()


@router.post('/get_order') 
async def get_coffee_shop(order_id:str=Body(embed=True))-> ServiceResponse:
    res = await order_database.get_order(order_id)
    return res


@router.post('/create_order')
async def create_coffee_shop(order:Order =Body(embed=True),userId:str = Depends(auth_user))->ServiceResponse:
    order.customer_id=userId
    res = await order_database.create_order(order)
    return res


