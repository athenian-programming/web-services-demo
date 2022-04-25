#!/usr/bin/env python3

import requests


def customers():
    host = 'http://localhost:8080'
    # host = 'https://athenian-ws-demo.herokuapp.com'

    resp = requests.get(f'{host}/customers')

    data = resp.json()

    cust_list = data['customers']

    for cust in cust_list:
        yield cust
