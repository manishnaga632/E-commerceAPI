# api/database/schemas/carts.py
from pydantic import BaseModel
from datetime import datetime

# Request schema: only product_id and quantity
class CartsCreate(BaseModel):
    product_id: int
    quantity: int

# Response schema: full response back to frontend
class CartsResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    created_at: datetime

    class Config:
        from_attributes = True
