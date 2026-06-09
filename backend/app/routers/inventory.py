from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.product import Product
from app.models.transaction import Transaction

from app.schemas.transaction import StockTransaction

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post("/stock-in")
def stock_in(
    transaction: StockTransaction,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == transaction.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.current_stock += transaction.quantity

    inventory_transaction = Transaction(
        product_id=transaction.product_id,
        quantity=transaction.quantity,
        transaction_type="IN"
    )

    db.add(inventory_transaction)

    db.commit()

    db.refresh(product)

    return {
        "message": "Stock added successfully",
        "current_stock": product.current_stock
    }


@router.post("/stock-out")
def stock_out(
    transaction: StockTransaction,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == transaction.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.current_stock < transaction.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    product.current_stock -= transaction.quantity

    inventory_transaction = Transaction(
        product_id=transaction.product_id,
        quantity=transaction.quantity,
        transaction_type="OUT"
    )

    db.add(inventory_transaction)

    db.commit()

    db.refresh(product)

    return {
        "message": "Stock removed successfully",
        "current_stock": product.current_stock
    }


@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):

    return db.query(
        Transaction
    ).order_by(
        Transaction.created_at.desc()
    ).all()