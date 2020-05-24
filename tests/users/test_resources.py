from apps.users.resources import SignUp
from apps.utils.enums import EStatus_Code
from apps.messages import (
                          MSG_INVALID_DATA,
                          MSG_ALREADY_EXISTS,
                          MSG_NO_DATA
                          )


uri = '/api/users'
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


def test_post_json_empty_must_return_status_code_422(client):
    response = client.post(uri, json={})
    assert response.status_code == EStatus_Code.DATA_INVALID.value


def test_post_json_empty_must_return_message(client):
    response = client.post(uri, json={})
    assert response.json['message'] == MSG_NO_DATA


def test_post_json_one_arg_must_return_status_code_422(client):
    response = client.post(uri,
                           json=create_user(email=email)
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value


def test_post_json_two_arg_must_return_status_code_422(client):
    response = client.post(uri,
                           json=create_user(
                                            full_name=full_name,
                                            email=email,
                                            )
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value


def test_post_json_tree_arg_must_return_status_code_422(client):
    response = client.post(uri,
                           json=create_user(
                                            full_name=full_name,
                                            email=email,
                                            password=password
                                            )
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value


def test_post_json_data_invalid_must_return_message(client):
    response = client.post(uri, json=create_user(email=email))
    assert response.json['message'] == MSG_INVALID_DATA


# def test_post_json_valid_must_return_status_code_200(client):
#     response = client.post(uri, json=return_json_valid())
#     assert response.status_code == EStatus_Code.OK.value


# def test_post_json_valid_must_return_message_success(client):
#     response = client.post(uri, json=return_json_valid())

#     assert response.json['message'] == MSG_RESOURCE_CREATED.format('usuário')


def test_post_already_exists_must_return_status_code_400(client):
    response = client.post(uri, json=return_json_valid())

    assert response.status_code == EStatus_Code.BAD_REQUEST.value


def test_post_already_exists_must_return_message_warning(client):
    response = client.post(uri, json=return_json_valid())

    assert response.json['message'] == MSG_ALREADY_EXISTS.format('usuário')


def test_must_be_receive_object_json(client):
    response = client.post(uri, json={})

    assert isinstance(response.json, dict)


def test_must_be_receive_object_json_empty_and_return_schema(client):
    response = client.post(uri, json={})

    assert response.json == {'errors': [],
                             'message': 'Nenhum dado foi postado.',
                             'resource': 'Users'
                             }
