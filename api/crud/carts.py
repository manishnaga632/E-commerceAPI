# api/crud/carts.py
from sqlalchemy.orm import Session
from api.database.models.carts import Carts
from api.database.schemas.carts import CartsCreate
from datetime import datetime

def create_cart(db: Session, cart: CartsCreate, user_id: int):
    db_cart = Carts(
        user_id=user_id,
        product_id=cart.product_id,
        quantity=cart.quantity,
        created_at=datetime.utcnow()  # ✅ Always current time
    )
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def delete_cart(db: Session, cart_id: int):
    cart = db.query(Carts).filter(Carts.id == cart_id).first()
    if cart:
        db.delete(cart)
        db.commit()
        return {"success": True, "message": "cart deleted successfully"}
    return {"success": False, "message": "cart not found"}

def get_all_carts(db: Session):
    return db.query(Carts).all()
