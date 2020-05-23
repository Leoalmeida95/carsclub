# -*- coding: utf-8 -*-

# Python
import json
from apps import api
from flask_restful import Api
from apps.utils.enums import EStatus_Code

uri_base = '/'
uri_api = '/api'


def test_initial_response_302(client):
    response = client.get(uri_base)

    assert response.status_code == 302


def test_initial_redirect_to_path_api(client):
    response = client.get(uri_base)

    assert uri_api in response.headers['Location']


def test_index_response_status_code_ok(client):
    response = client.get(uri_api)

    assert response.status_code == EStatus_Code.OK.value


def test_home_response_hello(client):
    response = client.get(uri_api)
    data = json.loads(response.data.decode('utf-8'))

    assert data['site'] == 'Cars Club'


def test_home_response_json_content_type(client):
    content_type = "application/json"
    response = client.get(uri_api)

    assert response.content_type == content_type


def test_verify_if_api_instance_existes():
    result = getattr(api, 'api')

    assert isinstance(result, Api), 'deve ser Api do flask_restful'


def test_verify_if_api_has_configure_atribute():
    assert hasattr(api, 'configure_api'), 'api deve ter um configure_api'


def test_configure_api_must_be_invocable():
    atr = getattr(api, 'configure_api')

    assert hasattr(atr, '__call__'), 'o configure_api deve ser invocável'


def test_configure_api_must_be_have_argument():
    atr = getattr(api, 'configure_api')

    assert atr.__code__.co_argcount == 1, 'o configure_api\
                                            deve ter um argumento'
