from fastapi import APIRouter, Body, Depends
from models.coffe_shop import CoffeeShop
import database.coffe_shop_database as coffe_shop_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database

# Create an API router for coffee shop-related endpoints
router = APIRouter()

# Endpoint to get a coffee shop by its ID
@router.post('/get_coffee_shop')
async def get_coffee_shop(coffee_shop_id: str = Body(embed=True)) -> ServiceResponse:
    # Retrieve the coffee shop details from the database
    res = await coffe_shop_database.get_coffee_shop(coffee_shop_id)
    return res

# Endpoint to create a new coffee shop
@router.post('/create_coffee_shop')
async def create_coffee_shop(new_coffee_shop: CoffeeShop = Body(embed=True), userId: str = Depends(auth_user)) -> ServiceResponse:
    # Create the new coffee shop in the database
    res = await coffe_shop_database.create_coffee_shop(new_coffee_shop)
    return res

# Endpoint to get a list of all coffee shops
@router.post('/get_all_coffee_shops')
async def get_all_coffee_shops() -> ServiceResponse:
    # Retrieve all coffee shops from the database
    res = await coffe_shop_database.get_all_shops()
    return res
