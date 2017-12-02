#!/usr/bin/env python

import requests

r = requests.get('http://localhost:8080/customers', auth=('top', 'secret'))

print("Status code: {}".format(r.status_code))

for k, v in r.headers.iteritems():
    print("{}: {}".format(k, v))

data = r.json()
print("data type: {}\nvalue: {}\n".format(type(data), data))

cust_list = data['customers']
print("cust_list type: {}\nvalue: {}\n".format(type(cust_list), cust_list))

print("Customers:")
for cust in cust_list:
    for k, v in cust.iteritems():
        print("{}: {}".format(k, v))
    print("")
