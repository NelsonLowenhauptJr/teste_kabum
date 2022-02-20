from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE= "postgresql://postgres:password@localhost/kabum_db"
SQLALCHEMY_DATABASE="postgresql+psycopg2://postgres:password@localhost:5432/kabum_db"

engine= create_engine(SQLALCHEMY_DATABASE, echo= True)
SessionLocal= sessionmaker(bind=engine)
session= SessionLocal()
Base= declarative_base()

class Shipping_Methods(Base):
    __tablename__ = "shipping_methods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    price_index = Column(Float, nullable=False)
    delivery_time = Column(Integer, nullable=False)
    min_height = Column(Float, nullable=False)
    max_height = Column(Float, nullable=False)
    min_width = Column(Float, nullable=False)
    max_width = Column(Float, nullable=False)

shipping= [Shipping_Methods(
                name = "Entrega Ninja",
                price_index = 0.3,
                delivery_time = 6,
                min_height = 10,
                max_height = 200,
                min_width = 6,
                max_width = 140
                ),
            Shipping_Methods(
                name = "Entrega KaBuM",
                price_index = 0.2,
                delivery_time = 4,
                min_height = 5,
                max_height = 140,
                min_width = 13,
                max_width = 125
                )]

Base.metadata.create_all(engine)
session.add_all(shipping)
session.commit()
session.close()
