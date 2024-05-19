from fastapi import APIRouter, Body, Depends
from models.product import Product
import database.product_database as product_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database

# Create an API router for product-related endpoints
router = APIRouter()

# Endpoint to get a product by its ID
@router.post('/get_product')
async def get_product(product_id: str = Body(embed=True)) -> ServiceResponse:
    # Retrieve the product details from the database
    res = await product_database.get_product(product_id)
    return res

# Endpoint to create a new product
@router.post('/create_product')
async def create_product(product: Product = Body(embed=True), userId: str = Depends(auth_user)) -> ServiceResponse:
    # Create the new product in the database
    res = await product_database.create_product(product)
    return res
