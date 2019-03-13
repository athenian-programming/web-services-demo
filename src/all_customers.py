#!/usr/bin/env python

import requests


def main():
    resp = requests.get('http://localhost:8080/customers', auth=('top', 'secret'))

    print('Status code: {}'.format(resp.status_code))

    for k, v in resp.headers.iteritems():
        print('{}: {}'.format(k, v))

    data = resp.json()
    print('data type: {}\nvalue: {}\n'.format(type(data), data))

    cust_list = data['customers']
    print('cust_list type: {}\nvalue: {}\n'.format(type(cust_list), cust_list))

    print('Customers:')
    for cust in cust_list:
        for k, v in cust.iteritems():
            print('{}: {}'.format(k, v))
        print('')


if __name__ == "__main__":
    main()
