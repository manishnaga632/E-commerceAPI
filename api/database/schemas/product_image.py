from pydantic import BaseModel
from typing import Optional

# ✅ Schema for Creating a Product Image
class ProductImageCreate(BaseModel):
    product_id: int
    image: str  # Assuming image is stored as a URL or path

# ✅ Schema for Response
class ProductImageResponse(BaseModel):
    id: int
    product_id: int
    image: str

    class Config:
        from_attributes = True
