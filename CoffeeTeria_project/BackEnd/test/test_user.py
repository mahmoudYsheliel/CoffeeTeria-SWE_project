import requests
import json
import _test_config

# Base URL for the API
url = _test_config.get_api_url()
# Token for authentication
token = _test_config.get_token()

# Test for creating a user with a valid username and password
def test_create_user():
    res = requests.post(
        url + "/signup",
        json={"user": {"username": "mahmoud50", "password": "50"}},
    )
    # Check if the status code is 200 (OK)
    assert res.status_code == 200
    data = json.loads(res.content)
    # Check if the response contains the user_id
    assert data["data"]['user_id']

# Test for creating a user without a username
def test_create_user_no_userName():
    res = requests.post(
        url + "/signup",
        json={"user": {"password": "50"}},
    )
    # Check if the status code is 422 (Unprocessable Entity)
    assert res.status_code == 422

# Test for creating a user without a password
def test_create_user_no_password():
    res = requests.post(
        url + "/signup",
        json={"user": {"username": "mahmoud50"}},
    )
    # Check if the status code is 422 (Unprocessable Entity)
    assert res.status_code == 422

# Test for creating a user without user data
def test_create_user_no_user():
    res = requests.post(
        url + "/signup",
    )
    # Check if the status code is 422 (Unprocessable Entity)
    assert res.status_code == 422

# Test for obtaining a token with valid credentials
def test_get_token():
    data = {
        "username": 'hossam',
        "password": '2000'
    }
    res = requests.post(url + '/token', data=data)
    # Check if the response contains the access token
    assert res.json()['access_token']

# Test for obtaining a token without providing a username
def test_get_token_no_username():
    data = {
        "password": '2000'
    }
    res = requests.post(url + '/token', data=data)
    # Check if the status code is 422 (Unprocessable Entity)
    assert res.status_code == 422

# Test for obtaining a token without providing a password
def test_get_token_no_password():
    data = {
        "username": 'hossam'
    }
    res = requests.post(url + '/token', data=data)
    # Check if the status code is 422 (Unprocessable Entity)
    assert res.status_code == 422

# Test for obtaining a token with an incorrect password
def test_get_token_wrong_password():
    data = {
        "username": 'hossam',
        "password": '1000'
    }
    res = requests.post(url + '/token', data=data)
    # Check if the response status code is 404 (Not Found) when using wrong password
    assert res.json()['status_code'] == 404
