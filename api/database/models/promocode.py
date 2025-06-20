# from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime

# Base = declarative_base()

# class Promocode(Base):
#     __tablename__ = "promocodes"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     discount_type = Column(String, nullable=False)
#     discount_value = Column(Float, nullable=False)
#     status = Column(Boolean, default=True)
#     expiry_date = Column(Date, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime

# Base = declarative_base()

# class Promocode(Base):
#     __tablename__ = "promocodes"

#     # Primary key for the table
#     id = Column(Integer, primary_key=True, index=True)

#     # The promocode name, required field
#     name = Column(String, nullable=False, unique=True)

#     # Description of the promocode, optional field
#     description = Column(String, nullable=True)

#     # The type of discount, either "percentage" or "fixed", required
#     discount_type = Column(String, nullable=False)

#     # Discount value, required field (for example, 10 for 10%)
#     discount_value = Column(Float, nullable=False)

#     # Status of the promocode, whether it is active or not (default is True)
#     status = Column(Boolean, default=True)

#     # Expiry date of the promocode, required
#     expiry_date = Column(Date, nullable=False)

#     # Timestamps for when the promocode is created and updated
#     created_at = Column(DateTime, default=datetime.utcnow)

#     # Automatically updates the `updated_at` field when the row is modified
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     def __repr__(self):
#         return f"<Promocode(id={self.id}, name={self.name}, discount_type={self.discount_type}, discount_value={self.discount_value}, status={self.status}, expiry_date={self.expiry_date}, created_at={self.created_at}, updated_at={self.updated_at})>"


from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.sql import func
from api.database.connection import Base  # Use centralized Base instead of declaring again

class Promocode(Base):
    __tablename__ = "promocodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    discount_type = Column(String(20), nullable=False)  # Expect values: 'percentage' or 'fixed'
    discount_value = Column(Float, nullable=False)
    status = Column(Boolean, default=True)
    expiry_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

   
