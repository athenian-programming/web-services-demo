#!/usr/bin/env python

import argparse

import requests

NAME = 'name'

# Parse cli args
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', required=True, dest=NAME, help='Customer name')
args = vars(parser.parse_args())

resp = requests.get('http://localhost:8080/customer_query', params={'name': args[NAME]})

print('URL: {}\n'.format(resp.url))

data = resp.json()
cust_list = data['customers']

print('Customers:')
for cust in cust_list:
    for k, v in cust.iteritems():
        print('{}: {}'.format(k, v))
    print('')