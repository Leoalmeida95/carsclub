# -*- coding: utf-8 -*-

# Python
import json

def test_home_response_hello(client):
    """
    **Given** Luiza está acessando a API,
    **When** ela informa a rota/endpoint `/`,
    **Then** a api deve responder um objeto com a chave `['hello']`,
    **And** seu conteúdo deve ser `world by apps`
    """
    # Realiza uma requisição HTTP do tipo get para o endpoint /
    response = client.get('/')

    # Utilizamos a função loads do modulo json para retornar um dict
    # para a váriavel data.
    # Precisamos passar por parâmetro para essa função a resposta
    # retornada pelo servidor, através da váriavel response.data
    # e decodificar para utf-8
    data = json.loads(response.data.decode('utf-8'))

    # Fazemos o teste de asserção pela chave 'hello'
    assert data['hello'] == 'world by apps'