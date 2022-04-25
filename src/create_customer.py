#!/usr/bin/env python3

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

    host = 'http://localhost:8080'
    # host = 'https://athenian-ws-demo.herokuapp.com'

    resp = requests.post(f'{host}/customers', json={'name': args[NAME], 'address': args[ADDRESS]})

    print(f'URL: {resp.url}\n')

    data = resp.json()
    cust = data['customer']

    print('New customer:')
    for k, v in cust.items():
        print(f'{k}: {v}')
    print('')


if __name__ == "__main__":
    main()
