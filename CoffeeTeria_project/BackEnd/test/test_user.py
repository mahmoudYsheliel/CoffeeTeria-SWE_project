import requests
import json
import _test_config


url = _test_config.get_api_url()
token = _test_config.get_token()

def test_create_user():
    res = requests.post(
        url + "/signup",
        json={"user": {"username": "mahmoud50", "password": "50"}},

    )
    # check status code
    assert res.status_code == 200
    data = json.loads(res.content)
    # check if response contains id
    assert data["data"]['user_id']
    
    
def test_create_user_no_userName():
    res = requests.post(
        url + "/signup",
        json={"user": {"password": "50"}},

    )
    # check status code
    assert res.status_code == 422
    
    
def test_create_user_no_password():
    res = requests.post(
        url + "/signup",
        json={"user": {"username": "mahmoud50"}},

    )
    # check status code
    assert res.status_code == 422


def test_create_user_no_user():
    res = requests.post(
        url + "/signup",

    )
    # check status code
    assert res.status_code == 422

def test_get_token():
    data = {
        "username": 'hossam',
        "password": '2000'
    }
    res=requests.post( url+'/token', data=data)
    assert res.json()['access_token']

def test_get_token_no_username():
    data = {
        "password": '2000'
    }
    res=requests.post( url+'/token', data=data)
        # check status code
    assert res.status_code == 422 

def test_get_token_no_password():
    data = {
        "username": 'hossam'
    }
    res=requests.post( url+'/token', data=data)
        # check status code
    assert res.status_code == 422 

def test_get_token_wrong_password():
    data = {
        "username": 'hossam',
        "password": '1000'
    }
    res=requests.post( url+'/token', data=data)
        # check status code
        
    assert res.json()['status_code']==404