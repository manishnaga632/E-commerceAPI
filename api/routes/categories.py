from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from api.database.connection import get_db
from api.database.schemas.categories import CategoryCreate, CategoryUpdate, CategoryResponse
from api.crud.category import create_category, delete_category, get_all_category, update_category

# API Router for category endpoints
router = APIRouter()

@router.post("/add", response_model=CategoryResponse)
def add(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        # Create the category in the database
        db_category = create_category(db, category)
        # Directly return the db_category, Pydantic will handle serialization automatically
        return db_category
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error adding category to database: {str(e)}")

@router.put("/update/{category_id}", response_model=CategoryResponse)
def update(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):
    try:
        # Update the category and get the result
        result = update_category(db, category_id, category_data)
        
        if isinstance(result, dict) and "success" in result and not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        
        # If update_category returns a category directly
        if hasattr(result, "id"):  # Checking if result is a category model
            return result  # Return the updated category, which will be automatically serialized by Pydantic
        
        # If update_category doesn't return category but just a success flag
        raise HTTPException(status_code=500, detail="Unexpected response from update_category")

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error updating category: {str(e)}")


@router.delete("/delete/{category_id}", response_model=dict)
def delete(category_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_category(db, category_id)
        if not result['success']:
            raise HTTPException(status_code=404, detail=result['message'])
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error deleting category: {str(e)}")

@router.get("/all_category", response_model=List[CategoryResponse])
def list_category(db: Session = Depends(get_db)):
    try:
        categories = get_all_category(db)
        # Pydantic will handle serialization automatically for each category
        return categories  # No need for .from_orm(), Pydantic will handle it
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching categories: {str(e)}")
