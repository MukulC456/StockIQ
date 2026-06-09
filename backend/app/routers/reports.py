from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.product import Product

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/inventory-value")
def inventory_value_report(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()

    report = []

    total_inventory_value = 0

    for product in products:

        value = (
            product.current_stock *
            product.cost_price
        )

        total_inventory_value += value

        report.append({
            "product": product.name,
            "stock": product.current_stock,
            "cost_price": product.cost_price,
            "inventory_value": value
        })

    return {
        "total_inventory_value":
        total_inventory_value,
        "products":
        report
    }

@router.get("/low-stock")
def low_stock_report(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()

    report = []

    for product in products:

        if product.current_stock <= product.minimum_stock:

            report.append({
                "product": product.name,
                "current_stock": product.current_stock,
                "minimum_stock": product.minimum_stock
            })

    return report