from apps.users.resources import SignUp
from apps.utils.enums import EStatus_Code

uri = '/api/users'


def test_must_be_invocable(client):
    atr = getattr(SignUp, 'post')

    assert hasattr(atr, '__call__'), 'o atributo deve ser invocável'


def test_must_be_return_object_json(client):

    response = client.post(uri, json={})

    assert response.status_code in [EStatus_Code.OK.value,
                                    EStatus_Code.EXCEPTION.value,
                                    EStatus_Code.DATA_INVALID.value,
                                    EStatus_Code.BAD_REQUEST.value
                                    ]
