from models.order import Order
from models.runtime import ServiceResponse
from database.mongo_driver import get_database, validate_bson_id

# Function to create an order
async def create_order(order: Order) -> ServiceResponse:
    amount = 0
    # Calculate the total amount for the order
    for item in order.details:
        bson_id = validate_bson_id(item.product_id)
        product = await get_database().get_collection('product').find_one({'_id': bson_id}, {'price': 1})
        price = product['price']
        amount += price * item.count
    order.amount = amount
    
    # Retrieve the customer's balance
    bson_id = validate_bson_id(order.customer_id)
    balance = await get_database().get_collection('user').find_one({'_id': bson_id})
    balance = balance['balance']
    
    # Check if the customer has enough balance to place the order
    if balance < amount:
        return ServiceResponse(success=False, msg="not enough money", status_code=409)
    
    # Insert the order into the database
    mdb_result = await get_database().get_collection("order").insert_one(order.model_dump())
    order_id = str(mdb_result.inserted_id)
    
    # Update the customer's balance after placing the order
    if order_id:
        await get_database().get_collection('user').update_one({'_id': bson_id}, {'$set': {'balance': balance - amount}})
        return ServiceResponse(data={"order_id": order_id})
    return ServiceResponse(success=False, msg="couldn't add order", status_code=409)

# Function to get an order by its ID
async def get_order(order_id: str) -> ServiceResponse:
    bson_id = validate_bson_id(order_id)
    if not bson_id:
        return ServiceResponse(status_code=400, msg="Bad order ID")
    
    # Retrieve the order details from the database
    order = await get_database().get_collection("order").find_one(
        {"_id": bson_id},
        {
            "_id": 0,
            "id": {"$toString": "$_id"},
            "coffee_shop_id": 1,
            "customer_id": 1,
            "created_at": 1,
            "type": 1,
            "amount": 1,
            "details": 1,
        },
    )
    
    # Check if the order exists
    if not order:
        return ServiceResponse(success=False, status_code=404, msg="Order not found")
    
    return ServiceResponse(data={"order": order})
