from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class ShippingMethods(Base):
    __tablename__ = "shipping_methods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    price_index = Column(Float, nullable=False)
    delivery_time = Column(Integer, nullable=False)
    min_height = Column(Float, nullable=False)
    max_height = Column(Float, nullable=False)
    min_width = Column(Float, nullable=False)
    max_width = Column(Float, nullable=False)