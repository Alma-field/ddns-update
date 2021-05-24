from ddns import OnamaeCom

if __name__ == "__main__":
    from argparse import ArgumentParser
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--service <service>]'
    )
    service_list = ['onamaecom']
    arg_parser.add_argument('-s', '--service', choices=service_list)
    options = arg_parser.parse_args()

    if options.service == 'onamaecom':
        ddns = OnamaeCom()
    else:
        raise NotImplementedError('NotImplementedError')

    old_ip = ddns.get_dnsip()
    new_ip = ddns.get_nowip()

    if not old_ip == new_ip:
        ddns.updateip(new_ip)
