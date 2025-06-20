# from sqlalchemy import Column, Integer, Float,String,DateTime,func,ForeignKey
# from api.database.connection import Base

# class Products(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, index=True)
#     # category_id = Column(Integer, primary_key=True, index=True)
#     category_id = Column(Integer, ForeignKey("categories.id"), index=True)  # ForeignKey referencing categories table

#     name = Column(String(100), nullable=False)
#     slug = Column(String(100), nullable=True)
#     description = Column(String(100), nullable=False)
#     mrp=Column(Float)
#     net_price=Column(Float)
#     quantity_in_stock=Column(Integer)
#     image = Column(String(100), nullable=False)
#     product_cat =Column(String(200),nullable=False)
#     created_at=Column(DateTime,default=func.now())
#     updated_at = Column(DateTime, nullable=True)    

   


from sqlalchemy import Column, Integer, Float, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False, index=True)

    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=True)
    description = Column(String(255), nullable=False)
    mrp = Column(Float, nullable=False)
    net_price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)
    image = Column(String(255), nullable=False)
    product_cat = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # ✅ Relationship with Categories
    category = relationship("Categories", back_populates="products")

    

    # ✅ Relationship with Carts
    carts = relationship("Carts", back_populates="product")

    wishlist = relationship("Wishlist", back_populates="product")



