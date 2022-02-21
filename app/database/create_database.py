from models import Base, ShippingMethods
from database import engine, get_session_local

session= get_session_local()

shipping= [ShippingMethods(
                name = "Entrega Ninja",
                price_index = 0.3,
                delivery_time = 6,
                min_height = 10,
                max_height = 200,
                min_width = 6,
                max_width = 140
                ),
            ShippingMethods(
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
