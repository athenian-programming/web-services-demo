#!/usr/bin/env python

import argparse

import requests

NAME = 'name'


def main():
    # Parse cli args
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True, dest=NAME, help='Customer name')
    args = vars(parser.parse_args())

    host = 'http://localhost:8080'
    # host = 'https://athenian-ws-demo.herokuapp.com

    resp = requests.get(f'{host}/customer_query', params={'name': args[NAME]})

    print(f'URL: {resp.url}\n')

    data = resp.json()

    print(f'data is: {data}\n')

    cust_list = data['customers']

    print('Customers:')
    for cust in cust_list:
        for k, v in cust.items():
            print(f'{k}: {v}')
        print('')


if __name__ == "__main__":
    main()
