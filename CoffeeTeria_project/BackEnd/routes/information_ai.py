from fastapi import APIRouter, Body, Depends
from models.information import Info
import database.information_database as information_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database

# Create an API router for information-related endpoints
router = APIRouter()

# Endpoint to get information
@router.post('/get_information')
async def get_information() -> ServiceResponse:
    # Retrieve information from the database
    res = await information_database.get_information()
    return res

# Endpoint to create new information
@router.post('/create_information')
async def create_information(information: Info = Body(embed=True), userId: str = Depends(auth_user)) -> ServiceResponse:
    # Create the new information in the database
    res = await information_database.create_information(information)
    return res
