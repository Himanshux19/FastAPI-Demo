from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Products(Base):

    __tablename__ = "product"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100))
    price = Column(Float)
    description = Column(String(250))
    quantity = Column(Integer)