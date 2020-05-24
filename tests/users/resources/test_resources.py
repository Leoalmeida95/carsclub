from json import dumps
from apps.users.resources import SignUp
from apps.utils.enums import EStatus_Code
from apps.messages import (
                          MSG_INVALID_DATA,
                          MSG_ALREADY_EXISTS,
                          MSG_NO_DATA
                          )

data = {}
endpoint = '/api/users'
password = "123456"
confirm_password = "123456"
full_name = "Leonardo Almeida da Silva"
email = "leodasdasdx@gmail.com"


def create_user(**kwargs):

    user = {}
    for key, value in kwargs.items():
        user[key] = value

    return user


def return_json_valid():
    return create_user(full_name=full_name,
                       email=email,
                       confirm_password=confirm_password,
                       password=password
                       )


def test_signup_post_must_be_invocable(client):
    atr = getattr(SignUp, 'post')
    assert hasattr(atr, '__call__'), 'o atributo deve ser invocável'


def test_post_json_empty_must_return_message_no_data(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint)
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_NO_DATA


def test_post_return_must_receive_object_json(client):
    response = client.post(endpoint)
    assert isinstance(response.json, dict)


def test_post_json_empty_must_return_status_code_422(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint,
                           data=dumps(dict('')),
                           content_type='application/json'
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_NO_DATA


def test_post_return_must_receive_object_json_empty_and_return_schema(client):
    response = client.post(endpoint)
    assert response.json == {'errors': [],
                             'message': 'Nenhum dado foi postado.',
                             'resource': 'Users'
                             }


def test_post_json_one_arg_must_return_status_code_422(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint,
                           data=dumps(dict(create_user(email=email))),
                           content_type='application/json'
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_INVALID_DATA


def test_post_json_two_arg_must_return_status_code_422(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint,
                           data=dumps(dict(
                                            create_user(
                                                        full_name=full_name,
                                                        email=email,
                                                        )
                                            )
                                      ),
                           content_type='application/json'
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_INVALID_DATA


def test_post_json_tree_arg_must_return_status_code_422(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint,
                           data=dumps(dict(
                                            create_user(
                                                        full_name=full_name,
                                                        email=email,
                                                        password=password
                                                        )
                                            )
                                      ),
                           content_type='application/json'
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_INVALID_DATA


def test_post_already_exists_must_return_bad_request(client):
    """
        Verifica o status code 400 e a menssagem
    """
    client.post(endpoint,
                data=dumps(dict(return_json_valid())),
                content_type='application/json'
                )
    resp2 = client.post(endpoint,
                        data=dumps(dict(return_json_valid())),
                        content_type='application/json'
                        )

    assert resp2.status_code == EStatus_Code.BAD_REQUEST.value
    assert resp2.json['message'] == MSG_ALREADY_EXISTS.format('usuário')


# def test_post_json_valid_must_return_status_code_200(client):
#     response = client.post(endpoint, json=return_json_valid())
#     assert response.status_code == EStatus_Code.OK.value


# def test_post_json_valid_must_return_message_success(client):
#     response = client.post(endpoint, json=return_json_valid())

#     assert response.json['message'] == MSG_RESOURCE_CREATED.format('usuário')
