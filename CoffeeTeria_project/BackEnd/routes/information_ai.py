from fastapi import APIRouter, Body,Depends
from models.information import Info
import database.information_database as information_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database


router = APIRouter()


@router.post('/get_information') 
async def get_coffee_shop()-> ServiceResponse:
    res = await information_database.get_information()
    return res


@router.post('/create_information')
async def create_coffee_shop(information:Info =Body(embed=True),userId:str = Depends(auth_user))->ServiceResponse:
    res = await information_database.create_information(information)
    return res


