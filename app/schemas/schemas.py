from pydantic import BaseModel, Field

class Product(BaseModel):

    class Size(BaseModel):
        altura: float
        largura: float
        
    dimensao: Size
    peso: float= Field(gt=0)

class Shipping(BaseModel):
    nome: str
    valor_frete: str
    prazo_dias: int

    class Config:
        orm_mode= True