from pydantic import BaseModel


class ProductCreate(BaseModel):

    sku: str

    name: str

    description: str

    cost_price: float

    selling_price: float

    minimum_stock: int

    category_id: int


class ProductResponse(BaseModel):

    id: int

    sku: str

    name: str

    description: str

    cost_price: float

    selling_price: float

    current_stock: int

    minimum_stock: int

    category_id: int

    model_config = {
        "from_attributes": True
    }