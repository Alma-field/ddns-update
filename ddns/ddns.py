from requests import get

#environment vars config 環境変数設定
# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv('./.env', encoding='utf-8')
from os import environ

class DDNS():
    def __init__(self):
        self.user_id = environ['USER_ID']
        self.password = environ['PASSWORD']
        self.hosts = environ['HOSTS'].split(';')
        self.domain = environ['DOMAIN']

    def updateip(self):
        raise NotImplementedError('NotImplementedError')

    def get_nowip(self):
        try:
            url = 'https://webinfo.alma-field.com/ipaddress'
            response = get(url).json()
        except:
            url = 'https://alma-webinfo.herokuapp.com/ipaddress'
            response = get(url).json()
        ipaddress = response['value']
        return ipaddress

    def get_dnsip(self):
        if self.hosts[0] == '':
            domain = self.domain
        else:
            domain = f'{self.hosts[0]}.{self.domain}'
        url = f'https://dns.google.com/resolve?name={domain}&type=A'
        data = get(url).json()
        return data['Answer'][0]['data']
