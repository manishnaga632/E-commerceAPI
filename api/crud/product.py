from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from api.database.models.products import Products
from api.database.schemas.products import ProductsCreate, ProductsUpdate

# ✅ Create Product

def create_product(db: Session, product: ProductsCreate):
    created_at = product.created_at or datetime.utcnow()
    updated_at = product.updated_at or datetime.utcnow()

    # Auto-generate slug from name (replace spaces with hyphens and lowercase)
    slug = product.name.lower().replace(" ", "-")

    db_product = Products(
        category_id=product.category_id,
        name=product.name,
        slug=slug,
        description=product.description,
        mrp=product.mrp,
        net_price=product.net_price,
        quantity_in_stock=product.quantity_in_stock,
        image=product.image,
        product_cat=product.product_cat,
        created_at=created_at,
        updated_at=updated_at,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# ✅ Update Product by ID

def update_product(db: Session, product_id: int, updated_data: ProductsUpdate):
    product = db.query(Products).filter(Products.id == product_id).first()
    if not product:
        return None

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(product, key, value)

    # If name is updated, regenerate slug
    if "name" in updated_data.dict(exclude_unset=True):
        product.slug = updated_data.name.lower().replace(" ", "-")

    product.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(product)
    return product

# ✅ Delete Product by Slug

def delete_product(db: Session, slug: str):
    product = db.query(Products).filter(Products.slug == slug).first()
    if product:
        db.delete(product)
        db.commit()
        return {"success": True, "message": "Product deleted successfully"}
    return {"success": False, "message": "Product not found"}

# ✅ Delete Product by ID

def delete_product_by_id(db: Session, product_id: int):
    product = db.query(Products).filter(Products.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"success": True, "message": "Product deleted successfully"}
    return {"success": False, "message": "Product not found"}

# ✅ Get All Products

def get_all_products(db: Session):
    return db.query(Products).all()

# ✅ Get Single Product by ID

def get_product_by_id(db: Session, product_id: int):
    return db.query(Products).filter(Products.id == product_id).first()

# ✅ Get Single Product by Slug

def get_product_by_slug(db: Session, slug: str):
    return db.query(Products).filter(Products.slug == slug).first()

# ✅ Get Products by Category

def get_products_by_category(db: Session, product_cat: str):
    return db.query(Products).filter(Products.product_cat == product_cat).all()