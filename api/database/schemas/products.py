from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True




class ProductsCreate(BaseModel):
    category_id: int
    name: str
    description: str
    mrp: float
    net_price: float
    quantity_in_stock: int
    image: str
    product_cat: str
    created_at: datetime
    updated_at: datetime
    slug: Optional[str] = None  # Add slug as optional field

    class Config:
        from_attributes = True



class ProductsUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    mrp: Optional[float] = None
    net_price: Optional[float] = None
    quantity_in_stock: Optional[int] = None
    image: Optional[str] = None
    product_cat: Optional[str] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ProductsResponse(BaseModel):
    id: int
    category_id: int
    name: str
    slug: str
    description: str
    mrp: float
    net_price: float
    quantity_in_stock: int
    image: str
    product_cat: str
    created_at: datetime
    updated_at: datetime
    category: CategoryResponse

    class Config:
        from_attributes = True
