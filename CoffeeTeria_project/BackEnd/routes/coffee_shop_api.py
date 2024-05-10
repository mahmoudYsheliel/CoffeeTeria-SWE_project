from fastapi import APIRouter, Body,Depends
from models.coffe_shop import CoffeeShop
import database.coffe_shop_database as coffe_shop_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database


router = APIRouter()


@router.post('/get_coffee_shop') 
async def get_coffee_shop(coffee_shop_id:str=Body(embed=True))-> ServiceResponse:
    res = await coffe_shop_database.get_coffee_shop(coffee_shop_id)
    return res


@router.post('/create_coffee_shop')
async def create_coffee_shop(new_coffee_shop:CoffeeShop =Body(embed=True),userId:str = Depends(auth_user))->ServiceResponse:
    res = await coffe_shop_database.create_coffee_shop(new_coffee_shop)
    return res



@router.post('/get_all_coffee_shops') 
async def get_all_coffee_shops()-> ServiceResponse:
    res = await coffe_shop_database.get_all_shops()
    return res