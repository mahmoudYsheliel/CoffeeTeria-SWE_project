import requests
import json

# Server address and port configuration
_SERVER_ADDR = '127.0.0.1'
_SERVER_PORT = 8000

# Function to get the base API URL
def get_api_url():
    return f"http://{_SERVER_ADDR}:{_SERVER_PORT}"

# Function to get the file server URL
def get_file_server_url():
    return f"http://{_SERVER_ADDR}:{_SERVER_PORT}"

# Function to obtain an access token from the authentication endpoint
def get_token():
    url = f"http://{_SERVER_ADDR}:{_SERVER_PORT}/token"  # Token endpoint URL
    data = {
        "username": 'hossam',  # Username for authentication
        "password": '2000'     # Password for authentication
    }
    res = requests.post(url, data=data)  # Send POST request to obtain token
    return res.json()['access_token']    # Extract and return the access token from the response
