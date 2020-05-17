def test_admin_user_page_list_has_method_get_response_200(client):
    result = client.get('/api/admin/users/page/1')
    assert result.status_code == 200
