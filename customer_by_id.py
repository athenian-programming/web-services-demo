#!/usr/bin/env python

import requests

r = requests.get('http://localhost:8080/customers/1')

print("URL: {}\n".format(r.url))

data = r.json()
cust = data['customer']

print("Customer:")
for k, v in cust.iteritems():
    print("{}: {}".format(k, v))
print("")
