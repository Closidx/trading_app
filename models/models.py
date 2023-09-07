from datetime import datetime

from sqlalchemy import Column, Table, Integer, JSON, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=False)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("role.id"))
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
