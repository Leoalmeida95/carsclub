# -*- coding: utf-8 -*-

# Python
import json
from apps import api
from flask_restful import Api


def test_initial_response_302(client):
    response = client.get('/')

    assert response.status_code == 302


def test_initial_redirect_to_path_api(client):
    response = client.get('/')

    assert '/api' in response.headers['Location']


def test_index_response_200(client):
    response = client.get('/api')

    assert response.status_code == 200


def test_home_response_hello(client):
    response = client.get('/api')
    data = json.loads(response.data.decode('utf-8'))

    assert data['site'] == 'Cars Club'


def test_home_response_json_content_type(client):
    content_type = "application/json"
    response = client.get('/api')

    assert response.content_type == content_type


def test_verify_if_api_instance_existes(client):
    result = getattr(api, 'api')

    assert isinstance(result, Api)


def test_verify_if_api_has_configure_atribute(client):

    assert getattr(api, 'configure_api')
