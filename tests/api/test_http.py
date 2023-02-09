import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    # намагаємось отримати інформацію про користувача "defunkt" на 'GitHub.com'
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/anstasiia_kovalenko')
    # намагаємось отримати інформацію про неіснуючого користувача "anstasiia_kovalenko" на 'GitHub.com'
    # assert r.status_code == 200 (Negative test = failed) тест не пройшов
    assert r.status_code == 404 # Negative test = пройшов (такого користувача не знайдено)