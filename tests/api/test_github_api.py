import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_non_exist(github_api):
    r = github_api.get_user('butenkosergii')
    # print(r) спочатку вивели директиву в термінал щоб отрімати message для статусу 404, потім взяли змінну 'message' для перевірки
    assert r['message'] == 'Not Found'
