

# api/routes/cart.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.carts import CartsCreate, CartsResponse
from api.crud.carts import create_cart, delete_cart, get_all_carts
from typing import List
from api.token import get_current_user  # ✅ your JWT user extractor
from api.database.models.user import User    # ✅ your User model
from api.database.models.carts import Carts  # ✅ Add this import

router = APIRouter()

@router.post("/add", response_model=CartsResponse)
def add_to_cart(
    cart: CartsCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_cart(db=db, cart=cart, user_id=current_user.id)

@router.delete("/delete/{cart_id}", response_model=dict)
def delete(cart_id: int, db: Session = Depends(get_db)):
    return delete_cart(db, cart_id)

@router.get("/all_carts", response_model=List[CartsResponse])
def list_carts(db: Session = Depends(get_db)):
    return get_all_carts(db)


@router.delete("/clear_all")
def clear_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db.query(Carts).filter(Carts.user_id == current_user.id).delete()
    db.commit()
    return {"success": True, "message": "Cart cleared successfully"}




