from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.schemas.wishlist import WishlistCreate, WishlistOut
from api.crud import wishlist as crud_wishlist
from api.database.connection import get_db
from typing import List

router = APIRouter()

@router.get("/get_all", response_model=List[WishlistOut])
def read_all_wishlist(db: Session = Depends(get_db)):
    return crud_wishlist.get_all_wishlist(db)

@router.post("/add_wishlist", response_model=WishlistOut)
def add_to_wishlist(wishlist: WishlistCreate, db: Session = Depends(get_db)):
    return crud_wishlist.add_to_wishlist(db, wishlist)

@router.delete("/delete_wishlist/{wishlist_id}", response_model=WishlistOut)
def delete_wishlist_item(wishlist_id: int, db: Session = Depends(get_db)):
    item = crud_wishlist.remove_from_wishlist(db, wishlist_id)
    if not item:
        raise HTTPException(status_code=404, detail="Wishlist item not found")
    return item


# http://127.0.0.1:8000/wishlist/get_all
# http://127.0.0.1:8000/wishlist/add_wishlist
# http://127.0.0.1:8000/wishlist/delete_wishlist/5


