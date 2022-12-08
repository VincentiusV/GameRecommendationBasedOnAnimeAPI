import requests

def get_bearer_token():
    url = 'https://tubeststwid.azurewebsites.net/login'
    data = {"username": "cent", "password": "cent"}
    response = requests.post(url, data=data)
    jsonresponse = response.json()
    bearertoken = str(jsonresponse['access_token'])
    return bearertoken

def get_structure(url: str):
    link = url
    headers = {"Authorization": f'Bearer {get_bearer_token()}'}
    response = requests.get(link, headers=headers)
    jsonresponse = response.json()
    return jsonresponse
