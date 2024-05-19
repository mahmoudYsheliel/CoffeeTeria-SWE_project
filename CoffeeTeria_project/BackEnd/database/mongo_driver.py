import motor.motor_asyncio
from bson import ObjectId

# Global variable to store the MongoDB client
mdb_client: motor.motor_asyncio.AsyncIOMotorClient | None = None

# Function to connect to MongoDB
async def mongodb_connect():
    connection_string = 'mongodb://localhost:27017'
    global mdb_client
    
    # Create a MongoDB client with a server selection timeout of 3000 ms
    mdb_client = motor.motor_asyncio.AsyncIOMotorClient(connection_string, serverSelectionTimeoutMS=3000)

# Function to get the database object
def get_database() -> motor.motor_asyncio.core.AgnosticDatabase | None:
    if mdb_client:
        # Return the database named 'CoffeTeria'
        return mdb_client.CoffeTeria
    return None

# Function to validate and convert a BSON ID string to an ObjectId
def validate_bson_id(bson_id: str) -> ObjectId | None:
    try:
        # Convert the string to an ObjectId
        return ObjectId(bson_id)
    except:
        # Return None if conversion fails
        return None
