from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class KPAForm(Base):
    __tablename__ = "kpa_forms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    document_path = Column(Text, nullable=False)