#!/usr/bin/env python

import requests


def customers():
    resp = requests.get('http://localhost:8080/customers')

    data = resp.json()

    cust_list = data['customers']

    for cust in cust_list:
        yield cust
