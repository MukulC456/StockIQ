from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.user import User
from app.models.category import Category

from app.routers.auth import router as auth_router
from app.routers.categories import router as category_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StockIQ API",
    version="0.1.0",
    description="AI-Powered Inventory Management System"
)

app.include_router(auth_router)
app.include_router(category_router)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "StockIQ Running"
    }