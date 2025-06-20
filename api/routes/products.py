from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.database.schemas.products import ProductsCreate, ProductsResponse, ProductsUpdate
from api.database.connection import get_db
import api.crud.product as crud

router = APIRouter()

# ✅ Create a product (slug auto-generate)
@router.post("/add", response_model=ProductsResponse)
def create_product_route(product: ProductsCreate, db: Session = Depends(get_db)):
    if not product.slug:  # If slug is not provided, generate it
        product.slug = product.name.lower().replace(" ", "-")
    return crud.create_product(db, product)


# ✅ Get all products
@router.get("/all_products", response_model=List[ProductsResponse])
def get_all_products_route(db: Session = Depends(get_db)):
    return crud.get_all_products(db)

# ✅ Get a product by ID
@router.get("/id/{product_id}", response_model=ProductsResponse)
def get_product_by_id_route(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# ✅ Get a product by slug
@router.get("/slug/{slug}", response_model=ProductsResponse)
def get_product_by_slug(slug: str, db: Session = Depends(get_db)):
    product = crud.get_product_by_slug(db, slug)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# ✅ Get products by category
@router.get("/category/all_products/{product_cat}", response_model=List[ProductsResponse])
def get_products_by_category(product_cat: str, db: Session = Depends(get_db)):
    return crud.get_products_by_category(db, product_cat)

# ✅ Delete product by slug
@router.delete("/delete/{slug}")
def delete_product_by_slug(slug: str, db: Session = Depends(get_db)):
    result = crud.delete_product(db, slug)
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

# ✅ Delete product by ID
@router.delete("/delete/id/{product_id}")
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"success": True, "message": "Product deleted successfully"}

# ✅ Update product by ID
@router.put("/update/{product_id}", response_model=ProductsResponse)
def update_product_route(product_id: int, updated_product: ProductsUpdate, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    updated = crud.update_product(db, product_id, updated_product)
    if not updated:
        raise HTTPException(status_code=400, detail="Product update failed")
    return updated
