import requests
import json


_SERVER_ADDR = '127.0.0.1'
_SERVER_PORT = 8000

def get_api_url():
    return f"http://{_SERVER_ADDR}:{_SERVER_PORT}"


def get_file_server_url():
    return f"http://{_SERVER_ADDR}:{_SERVER_PORT}"

def get_token():
    url=f"http://{_SERVER_ADDR}:{_SERVER_PORT}/token"
    data = {
        "username": 'hossam',
        "password": '2000'
    }
    res=requests.post( url, data=data)
    return res.json()['access_token']
