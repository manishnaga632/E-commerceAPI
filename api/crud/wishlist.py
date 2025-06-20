from sqlalchemy.orm import Session
from api.database.models.wishlist import Wishlist
from api.database.schemas.wishlist import WishlistCreate
from datetime import datetime

def get_all_wishlist(db: Session):
    return db.query(Wishlist).all()

def add_to_wishlist(db: Session, wishlist_data: WishlistCreate):
    wishlist_item = Wishlist(
        user_id=wishlist_data.user_id,
        product_id=wishlist_data.product_id,
        created_at=datetime.utcnow()
    )
    db.add(wishlist_item)
    db.commit()
    db.refresh(wishlist_item)
    return wishlist_item

def remove_from_wishlist(db: Session, wishlist_id: int):
    wishlist_item = db.query(Wishlist).filter(Wishlist.id == wishlist_id).first()
    if wishlist_item:
        db.delete(wishlist_item)
        db.commit()
    return wishlist_item
