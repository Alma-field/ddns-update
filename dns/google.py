from requests import get

def get_ip(domain):
    # https://8.8.8.8 -> https://dns.google.com
    url = f'https://8.8.8.8/resolve?name={domain}&type=A'
    data = get(url).json()
    return data['Answer'][0]['data']
