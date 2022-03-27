from requests import get

class DDNS():
    def __init__(self):
        from os import environ
        self.user_id = environ['USER_ID']
        self.password = environ['PASSWORD']

    def updateip(self):
        raise NotImplementedError('NotImplementedError')

    def get_dnsip(self):
        if self.hosts[0] == '':
            domain = self.domain
        else:
            domain = f'{self.hosts[0]}.{self.domain}'
        url = f'https://dns.google.com/resolve?name={domain}&type=A'
        data = get(url).json()
        return data['Answer'][0]['data']
