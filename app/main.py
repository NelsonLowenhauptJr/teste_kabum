from math import prod
from re import A
from typing import List
from zoneinfo import available_timezones
from fastapi import FastAPI, status

from database.models import ShippingMethods
from database.database import get_session_local as SessionLocal
from schemas.schemas import Product, Shipping


app= FastAPI(title="Teste Kabum", version=0.015)
session= SessionLocal()

class ProcessShippingMethods:
   
    def __init__(self, product: List[Product]):
        
        self.product= product
        self.all_methods= self.get_shipping_methods()
        self.available_methods= self.check_if_shipping_method_is_available_for_dimensions()
        self.final_methods= self.creating_shipping()
    
    def get_shipping_methods(self):

        shipping_methods = []
        for method in session.query(ShippingMethods).order_by(ShippingMethods.id):
            shipping_methods.append({
                                    "id": method.id,
                                    "name": method.name,
                                    "price_index": method.price_index,
                                    "delivery_time": method.delivery_time,
                                    "min_height": method.min_height,
                                    "max_height": method.max_height,
                                    "min_width": method.min_width,
                                    "max_width": method.max_width
                                    })
        session.close()

        return shipping_methods

    def check_if_shipping_method_is_available_for_dimensions(self):

        available_methods= []
        for i in range(len(self.all_methods)):
            if (self.all_methods[i]["min_height"] <= self.product.dimensao.altura <= self.all_methods[i]["max_height"]
                 and
                self.all_methods[i]["min_width"] <= self.product.dimensao.largura <= self.all_methods[i]["max_width"]):
                
                available_methods.append(self.all_methods[i])

        return available_methods

    def creating_shipping(self):

        final_shipping_methods_list: Shipping= []
        if len(self.available_methods) <= 0:
            return final_shipping_methods_list

        

        for i in range(len(self.available_methods)):
            
            self.shipping_price= (self.product.peso *  self.available_methods[i]["price_index"]) / 10
            
            final_shipping_methods_list.append({
                                        "nome": self.available_methods[i]["name"],
                                        "valor_frete": round(self.shipping_price, 2),
                                        "prazo_dias": self.available_methods[i]["delivery_time"]
                                        })

        return final_shipping_methods_list

    def get_shipping_methods_list(self):

        return self.final_methods

@app.get("/")
def bem_vindo():
    """
    Essa página existe
    """

    return {"Bem vindo! Para mais informações acesse /docs"}

@app.post("/tipos-de-frete", response_model= List[Shipping], status_code= status.HTTP_202_ACCEPTED)
def tipos_de_frete(produto:Product):
    """
    Informe altura, largura em centímetros (cm) e peso em gramas (g),
     para retornar as opções de envio.
    """

    shipping_methods= ProcessShippingMethods(produto)

    return shipping_methods.get_shipping_methods_list()

