#!/usr/bin/env python

import argparse

import requests

NAME = 'name'
ADDRESS = 'address'


def main():
    # Parse cli args
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True, dest=NAME, help='Customer name')
    parser.add_argument('-a', '--address', required=True, dest=ADDRESS, help='Customer address')
    args = vars(parser.parse_args())

    resp = requests.post('http://localhost:8080/customers', json={'name': args[NAME], 'address': args[ADDRESS]})

    print(f'URL: {resp.url}\n')

    data = resp.json()
    cust = data['customer']

    print('New customer:')
    for k, v in cust.items():
        print(f'{k}: {v}')
    print('')


if __name__ == "__main__":
    main()
