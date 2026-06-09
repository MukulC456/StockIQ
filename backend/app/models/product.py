from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    sku = Column(
        String(50),
        unique=True,
        nullable=False
    )

    name = Column(String(100))

    description = Column(String)

    cost_price = Column(Float)

    selling_price = Column(Float)

    current_stock = Column(
        Integer,
        default=0
    )

    minimum_stock = Column(
        Integer,
        default=5
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    category = relationship("Category")