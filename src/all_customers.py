#!/usr/bin/env python3

import requests


def main():
    host = 'http://localhost:8080'
    # host = 'https://athenian-ws-demo.herokuapp.com'

    resp = requests.get(f'{host}/customers', auth=('top', 'secret'))

    print(f'Status code: {resp.status_code}')

    for k, v in resp.headers.items():
        print(f'{k}: {v}')

    data = resp.json()
    print(f'data type: {type(data)}\nvalue: {data}\n')

    cust_list = data['customers']
    print(f'cust_list type: {type(cust_list)}\nvalue: {cust_list}\n')

    print('Customers:')
    for cust in cust_list:
        for k, v in cust.items():
            print(f'{k}: {v}')
        print('')


if __name__ == "__main__":
    main()
