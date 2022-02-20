from pydantic import BaseModel, Field

class Size(BaseModel):
        altura: float
        largura: float

class Product(BaseModel):
   
    dimensao: Size
    peso: float= Field(gt=0)

class Shipping(BaseModel):
    nome: str
    valor_frete: float
    prazo_dias: int

    class Config:
        orm_mode= True