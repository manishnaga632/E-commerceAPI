from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from api.database.connection import Base

class ProductImage(Base):  # ✅ Class name should follow PascalCase
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)  # ✅ Ensure "products" is the correct table name

    image = Column(String(255), nullable=False)  # ✅ Increased length for long URLs

    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # ✅ Auto-update on changes
