from pydantic import BaseModel

class ProductCreate(BaseModel):

    sku: str

    name: str

    description: str

    cost_price: float

    selling_price: float

    minimum_stock: int

    category_id: int