from typing import List
from fastapi import FastAPI, status

from database.models import Shipping_Methods
from database.database import get_session_local as SessionLocal
from schemas.schemas import Product, Shipping


app= FastAPI(title="Teste Kabum", version=0.015)
session= SessionLocal()

def validator(input: List[Shipping]):
    
    query_return= []

    for instance in session.query(Shipping_Methods).order_by(Shipping_Methods.id):
        
        if (input.dimensao.altura >= instance.min_height and
            input.dimensao.altura <= instance.max_height and
            input.dimensao.largura >= instance.min_width and
            input.dimensao.largura <= instance.max_width):
              
            price= (input.peso * instance.price_index) / 10

            query_return.append({
                            "nome": instance.name,
                            "valor_frete": "{:0.2f}".format(round(price, 2)),
                            "prazo_dias": instance.delivery_time
                            })

    return query_return

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

    return validator(produto)
