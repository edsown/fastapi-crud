from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Client(Base):
    __tablename__ = "clients"
    id =  Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False) 
    email = Column(String, nullable=False)
    is_special = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,  server_default=text("now()"))