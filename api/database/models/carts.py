
from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Carts(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    quantity = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, default=func.now())

  
       # Relationships
    product = relationship("Products", back_populates="carts")
    user = relationship("User", back_populates="carts")
