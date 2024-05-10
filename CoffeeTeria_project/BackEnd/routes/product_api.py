from fastapi import APIRouter, Body,Depends
from models.product import Product
import database.product_database as product_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database


router = APIRouter()


@router.post('/get_product') 
async def get_coffee_shop(product_id:str=Body(embed=True))-> ServiceResponse:
    res = await product_database.get_product(product_id)
    return res


@router.post('/create_product')
async def create_coffee_shop(product:Product =Body(embed=True),userId:str = Depends(auth_user))->ServiceResponse:
    res = await product_database.create_product(product)
    return res


