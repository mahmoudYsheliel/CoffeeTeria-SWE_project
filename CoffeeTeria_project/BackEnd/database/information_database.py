from models.information import Info
from models.runtime import ServiceResponse
from database.mongo_driver import get_database, validate_bson_id


async def create_information(information: Info) -> ServiceResponse:
    mdb_result = (
        await get_database()
        .get_collection("information")
        .insert_one(information.model_dump())
    )
    information_id = str(mdb_result.inserted_id)
    if information_id:
        return ServiceResponse(data={"information_id": information_id})
    return ServiceResponse(
        success=False, msg="couln't add information", status_code=409
    )


async def get_information() -> ServiceResponse:

    information = (
        await get_database()
        .get_collection("information")
        .find(
            {},
            {
                "_id": 0,
                "id": {"$toString": "$_id"},
                "title": 1,
                "description": 1,
                "type": 1,
            },
        ).to_list(length=None)
    )
    if not information:
        return ServiceResponse(
            success=False, status_code=404, msg="information Not Found"
        )
    return ServiceResponse(data={"information": information})

