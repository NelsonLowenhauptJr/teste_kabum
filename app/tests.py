import json
from fastapi.testclient import TestClient

from main import app

client= TestClient(app)

#--------Root Tests--------#

def test_root_status_code():
    '''
    Checks if status code = 200 OK
    
    '''
    
    response= client.get("/")

    assert response.status_code == 200

def test_root_message():
    '''
    Checks if the welcome message is displayed
    '''
    
    response= client.get("/")

    message= ["Bem vindo! Para mais informações acesse /docs"]

    assert response.json() == message

#--------Tipos de Frete Tests--------#

def test_tdf_status_code_for_weight_zero():
    '''
    POST weight must be major than zero
    '''

    data= {
            "dimensao":    
            {
            "altura": 150,
            "largura": 150
            },
            "peso": 0
            }

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert response.status_code == 422

def test_tdf_status_code_case_1():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 102,
            "largura": 40
            },
            "peso": 400
            }

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert response.status_code == 202

def test_tdf_returned_itens_case_1():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 102,
            "largura": 40
            },
            "peso": 400
            }

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert len(response.json()) == 2

def test_tdf_returned_message_case_1():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 102,
            "largura": 40
            },
            "peso": 400
            }

    message= [
            {
            "nome": "Entrega Ninja",
            "valor_frete": "12.00",
            "prazo_dias": 6
            },
            {
            "nome": "Entrega KaBuM",
            "valor_frete": "8.00",
            "prazo_dias": 4
            }
            ]

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert response.json() == message

def test_tdf_status_code_case_2():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 152,
            "largura": 50
            },
            "peso": 850
            }

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert response.status_code == 202

def test_tdf_returned_itens_case_2():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 152,
            "largura": 50
            },
            "peso": 850
            }

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert len(response.json()) == 1

def test_tdf_returned_message_case_2():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 152,
            "largura": 50
            },
            "peso": 850
            }

    message= [
           {
            "nome":"Entrega Ninja",
            "valor_frete": "25.50",
    	    "prazo_dias": 6
	}
            ]

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert response.json() == message

def test_tdf_status_code_case_3():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 230,
            "largura": 162
            },
            "peso": 5600
            }

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert response.status_code == 202

def test_tdf_returned_itens_case_3():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 230,
            "largura": 162
            },
            "peso": 5600
            }

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert len(response.json()) == 0

def test_tdf_returned_message_case_3():
    '''
    
    '''

    data= {
            "dimensao":    
            {
            "altura": 230,
            "largura": 162
            },
            "peso": 5600
            }

    message= []

    response= client.post(
                        "/tipos-de-frete", 
                        data=json.dumps(data),
                        headers={"Content-Type": "application/json"}
                        )

    assert response.json() == message
