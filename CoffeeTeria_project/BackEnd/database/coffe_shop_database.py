from models.coffe_shop import CoffeeShop
from models.runtime import ServiceResponse
from database.mongo_driver import get_database, validate_bson_id

# Function to create a new coffee shop
async def create_coffee_shop(coffee_shop: CoffeeShop) -> ServiceResponse:
    # Insert the coffee shop into the database
    mdb_result = await get_database().get_collection("coffee_shop").insert_one(coffee_shop.model_dump())
    coffee_shop_id = str(mdb_result.inserted_id)
    
    # Return the response with the inserted coffee shop ID
    if coffee_shop_id:
        return ServiceResponse(data={"coffee_shop_id": coffee_shop_id})
    return ServiceResponse(success=False, msg="couldn't add coffee_shop", status_code=409)

# Function to get a coffee shop by its ID
async def get_coffee_shop(coffee_shop_id: str) -> ServiceResponse:
    bson_id = validate_bson_id(coffee_shop_id)
    if not bson_id:
        return ServiceResponse(status_code=400, msg="Bad coffee_shop ID")

    # Retrieve the coffee shop details from the database
    coffee_shop = await get_database().get_collection("coffee_shop").find_one(
        {"_id": bson_id},
        {
            "_id": 0,
            "id": {"$toString": "$_id"},
            "name": 1,
            "city_name": 1,
            "location": 1,
            "open_time": 1,
            "close_time": 1,
            "image": 1,
            "products": 1,
            "contact_number": 1,
        }
    )
    
    # Check if the coffee shop exists
    if not coffee_shop:
        return ServiceResponse(success=False, status_code=404, msg="Coffee shop not found")
    
    return ServiceResponse(data={"coffee_shop": coffee_shop})

# Function to get all coffee shops
async def get_all_shops() -> ServiceResponse:
    # Retrieve all coffee shops from the database
    coffee_shops = await get_database().get_collection("coffee_shop").find(
        {},
        {
            "_id": 0,
            "id": {"$toString": "$_id"},
            "name": 1,
            "city_name": 1,
            "location": 1,
            "open_time": 1,
            "close_time": 1,
            "image": 1,
            "contact_number": 1,
        }
    ).to_list(length=None)
    
    # Check if any coffee shops are found
    if not coffee_shops:
        return ServiceResponse(success=False, status_code=404, msg="Coffee shops not found")
    
    return ServiceResponse(data={"coffee_shop": coffee_shops})
