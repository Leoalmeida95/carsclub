from json import dumps, loads
from apps.users.resources import SignUp, Activate
from apps.utils.enums import EStatus_Code
from apps.messages import (
                          MSG_INVALID_DATA,
                          MSG_ALREADY_EXISTS,
                          MSG_NO_DATA,
                          MSG_PASSWORD_WRONG,
                          MSG_DOES_NOT_EXIST,
                          #   MSG_RESOURCE_ACTIVE,
                          #   MSG_RESOURCE_CREATED
                          )

data = {}
endpoint_post = '/api/users'
endpoint_patch = 'api/users/activate/'

password = '123456'
confirm_password = '123456'
full_name = 'Leonardo Almeida da Silva'
email = 'leo@gmail.com'


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
    response = client.post(endpoint_post)
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_NO_DATA


def test_post_return_must_receive_object_json(client):
    response = client.post(endpoint_post)
    assert isinstance(response.json, dict)


def test_post_json_empty_must_return_status_code_422(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint_post,
                           data=dumps(dict('')),
                           content_type='application/json'
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_NO_DATA


def test_post_return_must_receive_object_json_empty_and_return_schema(client):
    response = client.post(endpoint_post)
    assert response.json == {'errors': [],
                             'message': 'Nenhum dado foi postado.',
                             'resource': 'Users'
                             }


def test_post_json_one_arg_must_return_status_code_422(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint_post,
                           data=dumps(dict(create_user(email=email))),
                           content_type='application/json'
                           )
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_INVALID_DATA


def test_post_json_two_arg_must_return_status_code_422(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.post(endpoint_post,
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
    response = client.post(endpoint_post,
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
    client.post(endpoint_post,
                data=dumps(dict(return_json_valid())),
                content_type='application/json'
                )
    resp2 = client.post(endpoint_post,
                        data=dumps(dict(return_json_valid())),
                        content_type='application/json'
                        )

    assert resp2.status_code == EStatus_Code.BAD_REQUEST.value
    assert resp2.json['message'] == MSG_ALREADY_EXISTS.format('usuário')


def test_post_password_wrong(client):
    """
        Verifica mensagem de validação de senha
    """
    response = client.post(endpoint_post,
                           data=dumps(dict(
                                            create_user(
                                                        full_name=full_name,
                                                        email=email,
                                                        password=password,
                                                        confirm_password="2"
                                                        )
                                            )
                                      ),
                           content_type='application/json'
                           )

    result = loads(response.data.decode('utf-8'))
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_INVALID_DATA
    assert result['errors']['password'] == MSG_PASSWORD_WRONG


# def test_post_json_valid_must_return_status_code_200(client):
#     response = client.post(endpoint_post, json=return_json_valid())
#     assert response.status_code == EStatus_Code.OK.value


# def test_post_json_valid_must_return_message_success(client):
#     response = client.post(endpoint_post, json=return_json_valid())

#     assert response.json['message'] == MSG_RESOURCE_CREATED.format('usuário')


def test_activate_patch_must_be_invocable(client):
    atr = getattr(Activate, 'patch')
    assert hasattr(atr, '__call__'), 'o atributo deve ser invocável'


def test_activate_patch_empty_must_return_message_no_data(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.patch(endpoint_patch + ' ')
    assert response.status_code == EStatus_Code.DATA_INVALID.value
    assert response.json['message'] == MSG_NO_DATA


def test_activate_patch_invalid_must_return_message_no_data(client):
    """
        Verifica o status code 422 e a menssagem
    """
    response = client.patch(endpoint_patch + '1')
    assert response.status_code == EStatus_Code.EXCEPTION.value
    assert response.json['message'] == MSG_INVALID_DATA


def test_activate_patch_not_exist_must_return_message_not_exists(client):
    """
        Verifica o status code 404 e a menssagem
    """
    response = client.patch(endpoint_patch + '5ebb765c61a8c16adafef46f')
    assert response.status_code == EStatus_Code.NOT_FOUND.value
    assert response.json['message'] == MSG_DOES_NOT_EXIST.format('Usuário')


# def test_activate_patch_valid_must_return_message_ok(client):
#     """
#         Verifica o status code 200 e a menssagem
#     """
#     result = client.post(endpoint_post,
#                          data=dumps(dict(return_json_valid())),
#                          content_type='application/json'
#                          )

#     data = loads(result.data.decode('utf-8'))
#     response = client.patch(endpoint_patch + data['id'])
#     assert response.status_code == EStatus_Code.OK.value
#     assert response.json['message'] == MSG_RESOURCE_ACTIVE.format('Usuário')
