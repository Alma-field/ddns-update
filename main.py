#environment vars config 環境変数設定
# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv('./.env', encoding='utf-8')
from os import environ

def get_ddns(options):
    if options.service == 'onamaecom':
        from ddns import OnamaeCom
        service = OnamaeCom()
    else:
        raise NotImplementedError('NotImplementedError')
    return service

def ipaddress(options):
    if options.ipaddress is not None:
        old_ip = options.ipaddress
    else:
        from ip import ALL
        for server in ALL:
            try:
                old_ip = server()
                break
            except:
                continue
        else:
            raise RuntimeError('Could not get the ip address.')
    return old_ip

def get_dns(options):
    if options.dns == 'google':
        from dns import google
        dns = google
    else:
        raise NotImplementedError('NotImplementedError')
    return dns

if __name__ == "__main__":
    from argparse import ArgumentParser
    args = ['[ --service <service>]']
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ''.join(args))
    from ddns import ALL as service_list
    arg_parser.add_argument('-s', '--service', choices=service_list, default='onamaecom')
    from validate.regexp import Regexp
    arg_parser.add_argument('-ip', '--ipaddress', choices=Regexp('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'))
    arg_parser.add_argument('-dns', '--dns', choices=['google'], default='google')
    arg_parser.add_argument('-f', '--force', action='store_true')
    options = arg_parser.parse_args()

    ddns = get_ddns(options)

    new_ip = ipaddress(options)
    print('Get now ip-address.')

    dns = get_dns(options)
    for domain in environ.get('DOMAINS', '').split('/'):
        old_ip = dns(domain.strip('.'))
        target, *host = domain.split('.')
        host = '.'.join(host)
        if options.force or not old_ip == new_ip:
            ddns.updateip(target, host, new_ip)
            print(f'{domain} updated.')
