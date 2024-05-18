from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import database.mongo_driver as mdb
from routes import user_api,coffee_shop_api,product_api,order_api,information_ai
from fastapi.staticfiles import StaticFiles
import uvicorn
@asynccontextmanager
async def lifespan(app: FastAPI):
    await mdb.mongodb_connect()
    yield
    # clean up resources here

app = FastAPI(
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user_api.router)
app.include_router(coffee_shop_api.router)
app.include_router(product_api.router)
app.include_router(order_api.router)
app.include_router(information_ai.router)

app.mount("/", StaticFiles(directory="public",
             html=True), name="public")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)