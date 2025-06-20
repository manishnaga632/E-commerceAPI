from sqlalchemy import Column, Integer, String,DateTime,func
from api.database.connection import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    mobile = Column(String(15), unique=True, nullable=False)
    role = Column(String(50), nullable=False, default="user")
    created_at=Column(DateTime,default=func.now())
    updated_at = Column(DateTime, nullable=True)  

    # Relationship to Wishlist
    wishlist = relationship("Wishlist", back_populates="user", cascade="all, delete-orphan")
  # Relationships
    carts = relationship("Carts", back_populates="user", cascade="all, delete-orphan")
