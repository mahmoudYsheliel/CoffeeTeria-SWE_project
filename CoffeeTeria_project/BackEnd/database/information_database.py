from models.information import Info
from models.runtime import ServiceResponse
from database.mongo_driver import get_database, validate_bson_id

# Function to create new information
async def create_information(information: Info) -> ServiceResponse:
    # Insert the information into the database
    mdb_result = await get_database().get_collection("information").insert_one(information.model_dump())
    information_id = str(mdb_result.inserted_id)
    
    # Return the response with the inserted information ID
    if information_id:
        return ServiceResponse(data={"information_id": information_id})
    return ServiceResponse(success=False, msg="couldn't add information", status_code=409)

# Function to retrieve all information
async def get_information() -> ServiceResponse:
    # Retrieve all information from the database
    information = await get_database().get_collection("information").find(
        {},
        {
            "_id": 0,
            "id": {"$toString": "$_id"},
            "title": 1,
            "description": 1,
            "type": 1,
        }
    ).to_list(length=None)
    
    # Check if any information is found
    if not information:
        return ServiceResponse(success=False, status_code=404, msg="Information not found")
    
    return ServiceResponse(data={"information": information})
