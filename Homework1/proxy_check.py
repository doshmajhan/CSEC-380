"""
    Program to scan a range of IP's for a proxy
    @author: Cameron Clark
"""

import argparse
import requests

def scan(address):
    """
        Scans a specific address for a proxy server

        :param address: The address/range to scan for
        :return proxy_list: the list of proxies that were found
    """


def main():
    """
        Main function to process args and run scan
    """
    parser = argparse.ArgumentParser(description="Scan a range of" \
                                    " IP's for a proxy")
    parser.add_argument('-i', dest='address', help='The address/range to scan',
                        required=True)

    args = parser.parse_args()
    address = args.address
    proxy_list = scan(address)

if __name__ == '__main__':
    main()
