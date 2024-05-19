from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import database.mongo_driver as mdb
from routes import user_api, coffee_shop_api, product_api, order_api, information_ai
from fastapi.staticfiles import StaticFiles
import uvicorn

# Async context manager for handling the application's lifespan events (startup and shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to the MongoDB database when the app starts
    await mdb.mongodb_connect()
    yield
    # Cleanup resources here when the app shuts down

# Create FastAPI app with a custom lifespan context manager
app = FastAPI(
    lifespan=lifespan,
)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow requests from any origin
    allow_methods=['*'],  # Allow all HTTP methods
    allow_headers=['*'],  # Allow all headers
)

# Include various API routers
app.include_router(user_api.router)
app.include_router(coffee_shop_api.router)
app.include_router(product_api.router)
app.include_router(order_api.router)
app.include_router(information_ai.router)

# Serve static files from the 'public' directory
app.mount("/", StaticFiles(directory="public", html=True), name="public")

# Entry point for running the app
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)  # Run the app on 0.0.0.0:8000
