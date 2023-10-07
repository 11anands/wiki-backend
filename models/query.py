from sqlalchemy.orm import Session
from . import models, schema


def get_drugs_v1(db: Session, drugs_id: int):
    return db.query(models.Drugs).filter(models.Drugs.id == drugs_id).first()


def get_drugs_v2(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Drugs).offset(skip).limit(limit).all()
