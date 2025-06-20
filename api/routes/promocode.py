# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from api.database.connection import get_db  # Assuming you have this

# from api.database.schemas.promocode import PromocodeCreate, PromocodeUpdate, PromocodeResponse
# import api.crud.promocode as promocode_crud

# router = APIRouter()

# @router.post("/addpromocode", response_model=PromocodeResponse)
# def create(data: PromocodeCreate, db: Session = Depends(get_db)):
#     return promocode_crud.create_promocode(db, data)

# @router.get("/all_promocode", response_model=list[PromocodeResponse])
# def get_all(db: Session = Depends(get_db)):
#     return promocode_crud.get_all_promocodes(db)

# @router.put("/update_promocode/{promocode_id}", response_model=PromocodeResponse)
# def update(promocode_id: int, data: PromocodeUpdate, db: Session = Depends(get_db)):
#     updated = promocode_crud.update_promocode(db, promocode_id, data)
#     if not updated:
#         raise HTTPException(status_code=404, detail="Promocode not found")
#     return updated

# @router.delete("/delete_promocode/{promocode_id}", response_model=PromocodeResponse)
# def delete(promocode_id: int, db: Session = Depends(get_db)):
#     deleted = promocode_crud.delete_promocode(db, promocode_id)
#     if not deleted:
#         raise HTTPException(status_code=404, detail="Promocode not found")
#     return deleted  


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from api.database.connection import get_db
import api.crud.promocode as promocode_crud
from api.database.schemas.promocode import PromocodeCreate, PromocodeUpdate, PromocodeResponse, PromocodeValidationResponse

router = APIRouter()

@router.post("/addpromocode", response_model=PromocodeResponse)
def create(data: PromocodeCreate, db: Session = Depends(get_db)):
    return promocode_crud.create_promocode(db, data)

@router.get("/all_promocode", response_model=list[PromocodeResponse])
def get_all(db: Session = Depends(get_db)):
    return promocode_crud.get_all_promocodes(db)

@router.put("/update_promocode/{promocode_id}", response_model=PromocodeResponse)
def update(promocode_id: int, data: PromocodeUpdate, db: Session = Depends(get_db)):
    updated = promocode_crud.update_promocode(db, promocode_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Promocode not found")
    return updated

@router.delete("/delete_promocode/{promocode_id}", response_model=PromocodeResponse)
def delete(promocode_id: int, db: Session = Depends(get_db)):
    deleted = promocode_crud.delete_promocode(db, promocode_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Promocode not found")
    return deleted  

# New route for promocode validation
@router.post("/validate_promocode", response_model=PromocodeValidationResponse)
def validate_promocode(promocode: str, db: Session = Depends(get_db)):
    promocode_data = promocode_crud.get_promocode_by_name(db, promocode)
    
    if not promocode_data:
        raise HTTPException(status_code=400, detail="Promocode not found")
    
    if promocode_data.status != True:  # Check if promocode is active
        raise HTTPException(status_code=400, detail="Promocode is not active")
    
    if promocode_data.expiry_date < datetime.utcnow().date():  # Compare with current date
        raise HTTPException(status_code=400, detail="Promocode has expired")
    
    return {"success": True, "discount_value": promocode_data.discount_value}
