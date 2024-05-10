from fastapi import APIRouter, Body,HTTPException,Depends
from models.todo import Todo,TodoSent
import database.todo_database as todo_database
from lib.crypto import auth_user
from models.runtime import ServiceResponse
from database.mongo_driver import get_database


router = APIRouter()


@router.post('/get_todos') 
async def get_todos(userId:int = Depends(auth_user))-> ServiceResponse:
    try:
        res = await todo_database.get_todos(userId)
        return res
    except:
        return ServiceResponse(status_code=402,success=False) 




@router.post('/delete_todo')
async def delete_todo(id:int = Body(embed=True),userId:int = Depends(auth_user))->ServiceResponse:
    try:
        res = await todo_database.delete_todo(id)
        todo_res = await todo_database.get_todo(id)
        todo=todo_res.data['todo']
        if todo:
            return ServiceResponse(success=False,msg="couldn't delete todo")
        return res
    except:
        return ServiceResponse(success=False,msg="couldn't delete todo")


@router.post('/update_todo')
async def update_todo(id:int=Body(embed=True),new_todo:TodoSent = Body(embed=True),userId:int = Depends(auth_user))->ServiceResponse:
    try:
        res = await todo_database.update_todo(id,new_todo.model_dump())
        return res
    except:
        return ServiceResponse(success=False,msg="couldn't update todo")


@router.post('/create_todo')
async def create_todo(new_todo:TodoSent =Body(embed=True),userId:int = Depends(auth_user)):
        id=await get_database().get_collection('todo').count_documents({})
        todo=Todo(id=id,userId=userId,title=new_todo.title,description=new_todo.description)
        res = await todo_database.create_todo(todo)
        return res

