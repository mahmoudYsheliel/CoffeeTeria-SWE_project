from models.user import User
from models.runtime import ServiceResponse
from database.mongo_driver import get_database, validate_bson_id
from lib.crypto import verify_password

# Function to create a new user
async def create_user(user: User) -> ServiceResponse:
    # Insert the user into the database
    mdb_result = await get_database().get_collection("user").insert_one(user.model_dump())
    user_id = str(mdb_result.inserted_id)
    return ServiceResponse(data={"user_id": user_id})

# Function to validate user credentials
async def validate_user(username: str, password: str) -> bool:
    # Check if the user exists in the database
    user = await get_database().get_collection("user").find_one({"username": username})
    if not user:
        return False
    
    # Verify the password
    if not verify_password(password, user['password']):
        return False
    return True

# Function to retrieve personal information of a user
async def personal_info(user_id: str):
    bson_id = validate_bson_id(user_id)
    if not bson_id:
        return ServiceResponse(success=False, msg="Couldn't Find User", status_code=409)
    
    # Retrieve user information from the database
    data = await get_database().get_collection('user').find_one(
        {'_id': bson_id},
        {
            '_id': 0,
            'balance': 1,
            'type': 1,
            'username': 1,
        }
    )
    if not data:
        return ServiceResponse(success=False, status_code=400, msg="Couldn't Find User")
    
    return ServiceResponse(data={'info': data})
