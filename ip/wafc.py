from requests import get

def get_ip():
    url = 'https://webinfo.alma-field.com/ipaddress'
    response = get(url).json()
    ipaddress = response['value']
    return ipaddress
