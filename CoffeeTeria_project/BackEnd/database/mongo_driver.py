import motor.motor_asyncio
from bson import ObjectId

mdb_client: motor.motor_asyncio.AsyncIOMotorClient | None = None

async def mongodb_connect():
    connection_string = 'mongodb://localhost:27017'
    global mdb_client
    
    mdb_client = motor.motor_asyncio.AsyncIOMotorClient(connection_string, serverSelectionTimeoutMS=3000)
    
    

def get_database() ->  motor.motor_asyncio.core.AgnosticDatabase | None:
    if mdb_client:
        return mdb_client.CoffeTeria
    return None

def validate_bson_id(bson_id: str) -> ObjectId | None:
    try:
        return ObjectId(bson_id)
    except:
        return None