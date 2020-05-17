from apps.users.resources_admin import AdminUserPageList


def test_admin_user_page_list_get_must_be_invocable(client):
    # garante que o a classe tem o metodo get e que ele é invocavel
    atr = getattr(AdminUserPageList, 'get')

    assert hasattr(atr, '__call__'), 'o atributo deve ser invocável'


def test_admin_user_page_list_get_response_200(client):
    result = client.get('/api/admin/users/page/1')
    assert result.status_code == 200


def test_admin_user_page_list_get_response_json_content_type(client):
    content_type = "application/json"
    response = client.get('/api/admin/users/page/1')

    assert response.content_type == content_type
