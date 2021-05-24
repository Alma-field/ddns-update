from ssl import wrap_socket
from socket import socket

from .ddns import DDNS

class OnamaeCom(DDNS):
    def __init__(self):
        super().__init__()

    def updateip(self, ipaddress):
        for host in self.hosts:
            sock = socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            s = wrap_socket(sock)
            s.connect(("ddnsclient.onamae.com", 65010))
            data = [
                'LOGIN',
                f'USERID:{self.user_id}',
                f'PASSWORD:{self.password}',
                '.',
                'MODIP',
                f'HOSTNAME:{host}',
                f'DOMNAME:{self.domain}',
                f'IPV4:{ipaddress}',
                '.',
                'LOGOUT',
                '.'
            ]
            for item in data:
                s.send(item.encode() + b'\r\n')
            s.close()
