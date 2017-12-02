#!/usr/bin/env python

import requests

r = requests.post('http://localhost:8080/customer_query', params={'name': 'Bill'})

print("URL: {}\n".format(r.url))

data = r.json()
cust_list = data['customers']

print("Customers:")
for cust in cust_list:
    for k, v in cust.iteritems():
        print("{}: {}".format(k, v))
    print("")
