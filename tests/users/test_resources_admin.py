from apps.users.resources_admin import AdminUserPageList
from apps.utils.enums import EStatus_Code

uri = '/api/admin/users/page/1'


def test_must_be_invocable(client):
    # garante que o a classe tem o metodo get e que ele é invocavel
    atr = getattr(AdminUserPageList, 'get')

    assert hasattr(atr, '__call__'), 'o atributo deve ser invocável'


def test_response_200(client):
    response = client.get(uri)

    assert response.status_code in [EStatus_Code.OK.value,
                                    EStatus_Code.EXCEPTION.value
                                    ]


def test_response_json_content_type(client):
    content_type = "application/json"
    response = client.get(uri)

    assert response.content_type == content_type
