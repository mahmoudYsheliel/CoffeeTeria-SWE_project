from fastapi import APIRouter, Body, Depends
from models.order import Order
import database.order_database as order_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database

# Create an API router for order-related endpoints
router = APIRouter()

# Endpoint to get an order by its ID
@router.post('/get_order')
async def get_order(order_id: str = Body(embed=True)) -> ServiceResponse:
    # Retrieve the order details from the database
    res = await order_database.get_order(order_id)
    return res

# Endpoint to create a new order
@router.post('/create_order')
async def create_order(order: Order = Body(embed=True), userId: str = Depends(auth_user)) -> ServiceResponse:
    # Set the customer_id of the order to the authenticated user's ID
    order.customer_id = userId
    # Create the new order in the database
    res = await order_database.create_order(order)
    return res
