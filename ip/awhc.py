from requests import get

def get_ip():
    url = 'https://alma-webinfo.herokuapp.com/ipaddress'
    response = get(url).json()
    ipaddress = response['value']
    return ipaddress
