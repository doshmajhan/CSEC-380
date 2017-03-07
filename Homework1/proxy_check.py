"""
    Program to scan a range of IP's for a proxy
    @author: Cameron Clark
"""

import argparse
import netaddr
import requests

def scan(address):
    """
        Scans a specific address for a proxy server

        :param address: The address/range to scan for
        :return proxy_list: the list of proxies that were found
    """
    proxy_list = []
    target_url = "http://google.com"
    base_status = requests.get(target_url)
    if base_status.status_code != 200:
        print "Site down"
        return None

    ports = [80, 888, 800, 880, 808, 8080, 8010]

    for ip in netaddr.IPNetwork(address):
        print(str(ip))
        for port in ports:
            proxies = {
                'http': str(ip) + ":" + str(port),
                'https': str(ip) + ":" + str(port)
            }

            try:
                test_status = requests.get(target_url, proxies=proxies, timeout=4)
                if test_status.status_code == 200:
                    print "%s:%s - IS a proxy: %d" % (str(ip), str(port), int(test_status.status_code))
                    proxy_list += [str(ip) + ":" + str(port)]
                    print test_status.text
                    break
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                print "%s:%s - not a proxy" % (str(ip), str(port))



        return proxy_list


def main():
    """
        Main function to process args and run scan
    """
    parser = argparse.ArgumentParser(description="Scan a range of" \
                                    " IP's for a proxy")
    parser.add_argument('-a', dest='address', help='The address/range to scan',
                        required=True)

    args = parser.parse_args()
    address = args.address
    proxy_list = scan(address)

if __name__ == '__main__':
    main()
