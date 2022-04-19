#!/usr/bin/env python

import argparse

import requests

ID = 'id'


def main():
    # Parse cli args
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--id', required=True, dest=ID, help='Customer ID')
    args = vars(parser.parse_args())

    host = 'http://localhost:8080'
    # host = 'https://athenian-ws-demo.herokuapp.com'

    # Make request
    resp = requests.get(f'{host}/customers/{args[ID]}')

    print(f'URL: {resp.url}\n')

    data = resp.json()
    cust = data['customer']

    print('Customer:')
    for k, v in cust.items():
        print(f'{k}: {v}')
    print('')


if __name__ == "__main__":
    main()
