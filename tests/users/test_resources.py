from apps.users.resources import SignUp
from apps.utils.enums import EStatus_Code

uri = '/api/users'

json_valido = {
            "confirm_password": "123456",
            "email": "leoasdas@gmail.com",
            "full_name": "Leonardo Almeida da Silva",
            "password": "123456"
            }


def test_must_be_invocable(client):
    atr = getattr(SignUp, 'post')

    assert hasattr(atr, '__call__'), 'o atributo deve ser invocável'


def test_must_be_return_status_code_valid(client):
    response = client.post(uri, json={})

    assert response.status_code in [EStatus_Code.OK.value,
                                    EStatus_Code.EXCEPTION.value,
                                    EStatus_Code.DATA_INVALID.value,
                                    EStatus_Code.BAD_REQUEST.value
                                    ]


def test_must_be_receive_object_json(client):
    response = client.post(uri, json={})

    assert isinstance(response.json, dict)


def test_must_be_receive_object_json_empty_and_return_schema(client):
    response = client.post(uri, json={})

    assert response.json == {'errors': [],
                             'message': 'Nenhum dado foi postado.',
                             'resource': 'Users'
                             }


def test_must_be_receive_object_json_valid_and_return_ok(client):
    response = client.post(uri, json=json_valido)

    assert response.json['message'] in ['Usuário criado(a).',
                                        'Já existe um(a)' +
                                        ' fornecedor com estes dados.']
