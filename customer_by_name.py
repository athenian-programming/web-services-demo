#!/usr/bin/env python

import argparse

import requests

NAME = 'name'


def main():
    # Parse cli args
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True, dest=NAME, help='Customer name')
    args = vars(parser.parse_args())

    resp = requests.get('http://localhost:8080/customer_query', params={'name': args[NAME]})

    print('URL: {}\n'.format(resp.url))

    data = resp.json()

    print('data is: {}\n'.format(data))

    cust_list = data['customers']

    print('Customers:')
    for cust in cust_list:
        for k, v in cust.items():
            print('{}: {}'.format(k, v))
        print('')


if __name__ == "__main__":
    main()
