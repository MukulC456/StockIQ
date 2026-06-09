from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db

from app.models.product import Product
from app.models.category import Category

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    total_products = db.query(
        Product
    ).count()

    total_categories = db.query(
        Category
    ).count()

    total_stock = db.query(
        func.sum(Product.current_stock)
    ).scalar()

    if total_stock is None:
        total_stock = 0

    return {
        "total_products": total_products,
        "total_categories": total_categories,
        "total_stock": total_stock
    }

@router.get("/low-stock")
def low_stock_items(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()

    low_stock_products = []

    for product in products:

        if product.current_stock <= product.minimum_stock:

            low_stock_products.append({
                "id": product.id,
                "name": product.name,
                "current_stock": product.current_stock,
                "minimum_stock": product.minimum_stock
            })

    return low_stock_products