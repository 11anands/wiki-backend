from sqlalchemy import Column, Date, String, ARRAY, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()


class Drugs(Base):
    __tablename__ = "drugs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    diseases = Column(ARRAY(String))
    description = Column(String)
    released = Column(Date, server_default=func.now())


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_created = Column(DateTime, server_default=func.now())
