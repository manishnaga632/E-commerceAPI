# from sqlalchemy.orm import Session
# from api.database.models.promocode import Promocode
# from api.database.schemas.promocode import PromocodeCreate, PromocodeUpdate
# from datetime import datetime

# def create_promocode(db: Session, data: PromocodeCreate):
#     new_code = Promocode(
#         name=data.name,
#         description=data.description,
#         discount_type=data.discount_type,
#         discount_value=data.discount_value,
#         status=data.status,
#         expiry_date=data.expiry_date,
#         created_at=datetime.utcnow(),
#         updated_at=datetime.utcnow()
#     )
#     db.add(new_code)
#     db.commit()
#     db.refresh(new_code)
#     return new_code

# def get_all_promocodes(db: Session):
#     return db.query(Promocode).all()

# def update_promocode(db: Session, promocode_id: int, data: PromocodeUpdate):
#     promocode = db.query(Promocode).filter(Promocode.id == promocode_id).first()
#     if not promocode:
#         return None

#     for field, value in data.dict().items():
#         setattr(promocode, field, value)
#     promocode.updated_at = datetime.utcnow()

#     db.commit()
#     db.refresh(promocode)
#     return promocode

# def delete_promocode(db: Session, promocode_id: int):
#     promocode = db.query(Promocode).filter(Promocode.id == promocode_id).first()
#     if not promocode:
#         return None

#     db.delete(promocode)
#     db.commit()
#     return promocode
from sqlalchemy.orm import Session
from api.database.models.promocode import Promocode
from api.database.schemas.promocode import PromocodeCreate, PromocodeUpdate
from datetime import datetime

def create_promocode(db: Session, data: PromocodeCreate):
    new_code = Promocode(
        name=data.name,
        description=data.description,
        discount_type=data.discount_type,
        discount_value=data.discount_value,
        status=data.status,
        expiry_date=data.expiry_date,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(new_code)
    db.commit()
    db.refresh(new_code)
    return new_code

def get_all_promocodes(db: Session):
    return db.query(Promocode).all()

def update_promocode(db: Session, promocode_id: int, data: PromocodeUpdate):
    promocode = db.query(Promocode).filter(Promocode.id == promocode_id).first()
    if not promocode:
        return None

    for field, value in data.dict().items():
        setattr(promocode, field, value)
    promocode.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(promocode)
    return promocode

def delete_promocode(db: Session, promocode_id: int):
    promocode = db.query(Promocode).filter(Promocode.id == promocode_id).first()
    if not promocode:
        return None

    db.delete(promocode)
    db.commit()
    return promocode

# New method for validating a promocode by name
def get_promocode_by_name(db: Session, promocode_name: str):
    promocode = db.query(Promocode).filter(Promocode.name == promocode_name).first()
    if not promocode:
        return None

    # Check if the promocode is active and not expired
    if promocode.status != True:  # Assuming status is a boolean (True = active)
        return None

    if promocode.expiry_date < datetime.utcnow().date():  # Compare with current date
        return None

    return promocode

