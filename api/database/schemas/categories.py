from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CategoryCreate(BaseModel):
    name: str
    created_at: Optional[datetime] = None  # Set to None, will be set by the backend
    updated_at: Optional[datetime] = None  # Set to None, will be updated by the backend

    class Config:
        from_attributes = True  # Allow ORM models to be converted to Pydantic models

class CategoryUpdate(BaseModel):
    name: Optional[str] = None  # Optional, since user might update only one field
    updated_at: Optional[datetime] = None  # Will be auto-set in the backend

    class Config:
        from_attributes = True

class CategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Allow ORM models to be converted to Pydantic models
