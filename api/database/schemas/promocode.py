# from pydantic import BaseModel
# from datetime import date, datetime
# from typing import Literal

# class PromocodeCreate(BaseModel):
#     name: str
#     description: str
#     discount_type: Literal["percentage", "fixed"]
#     discount_value: float
#     status: bool
#     expiry_date: date

# class PromocodeUpdate(BaseModel):
#     name: str
#     description: str
#     discount_type: Literal["percentage", "fixed"]
#     discount_value: float
#     status: bool
#     expiry_date: date

# class PromocodeResponse(BaseModel):
#     id: int
#     name: str
#     description: str
#     discount_type: Literal["percentage", "fixed"]
#     discount_value: float
#     status: bool
#     expiry_date: date
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         from_attributes = True



from pydantic import BaseModel
from datetime import date, datetime
from typing import Literal

class PromocodeCreate(BaseModel):
    name: str
    description: str
    discount_type: Literal["percentage", "fixed"]
    discount_value: float
    status: bool  # Assuming status is a boolean (active or inactive)
    expiry_date: date

class PromocodeUpdate(BaseModel):
    name: str
    description: str
    discount_type: Literal["percentage", "fixed"]
    discount_value: float
    status: bool
    expiry_date: date

class PromocodeResponse(BaseModel):
    id: int
    name: str
    description: str
    discount_type: Literal["percentage", "fixed"]
    discount_value: float
    status: bool
    expiry_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class PromocodeValidationResponse(BaseModel):
    success: bool
    discount_value: float
