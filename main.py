from ddns import OnamaeCom
#environment vars config 環境変数設定
# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv('./.env', encoding='utf-8')

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

if __name__ == "__main__":
    from argparse import ArgumentParser
    args = ['[ --service <service>]']
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ''.join(args))
    service_list = ['onamaecom']
    arg_parser.add_argument('-s', '--service', choices=service_list, default='onamaecom')
    options = arg_parser.parse_args()

    if options.service == 'onamaecom':
        ddns = OnamaeCom()
    else:
        raise NotImplementedError('NotImplementedError')

    old_ip = ddns.get_dnsip()
    new_ip = ipaddress(options)

    if not old_ip == new_ip:
        ddns.updateip(new_ip)
