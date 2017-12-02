#!/usr/bin/env python

import requests


def customers():
    r = requests.get('http://localhost:8080/customers')

    data = r.json()

    cust_list = data['customers']

    for cust in cust_list:
        yield cust
