from models.product import Product
from models.runtime import ServiceResponse
from models.runtime import ServiceResponse
from database.mongo_driver import get_database, validate_bson_id


async def create_product(product: Product) -> ServiceResponse:
    mdb_result = (
        await get_database()
        .get_collection("product")
        .insert_one(product.model_dump())
    )
    product_id = str(mdb_result.inserted_id)
    if product_id:
        return ServiceResponse(data={"product_id": product_id})
    return ServiceResponse(
        success=False, msg="couln't add product", status_code=409
    )


async def get_product(product_id: str) -> ServiceResponse:
    bson_id = validate_bson_id(product_id)
    if not bson_id:
        return ServiceResponse(status_code=400, msg="Bad product ID")

    product = (
        await get_database()
        .get_collection("product")
        .find_one(
            {"_id": bson_id},
            {
                "_id": 0,
                "id": {"$toString": "$_id"},
                "name": 1,
                "description": 1,
                "price": 1,
                "image": 1,
            },
        )
    )
    if not product:
        return ServiceResponse(
            success=False, status_code=404, msg="product Not Found"
        )
    return ServiceResponse(data={"product": product})

