from apps.users.resources_admin import AdminUserPageList


def test_admin_user_page_list_get_must_be_invocable(client):
    # garante que o a classe tem o metodo get e que ele é invocavel
    atr = getattr(AdminUserPageList, 'get')
    assert hasattr(atr, '__call__')


def test_admin_user_page_list_get_response_200(client):
    result = client.get('/api/admin/users/page/1')
    assert result.status_code == 200
