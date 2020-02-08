#!/usr/bin/env python
# Based on https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

import argparse
import logging
import os

from flask import Flask
from flask import Response
from flask import abort
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import request
from flask_httpauth import HTTPBasicAuth

from utils import setup_logging

PORT = 'port'
LOG_LEVEL = 'loglevel'

logger = logging.getLogger(__name__)

auth = HTTPBasicAuth()
http = Flask(__name__)


@auth.get_password
def get_password(username):
    if username == 'top':
        return 'secret'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@http.route('/')
def root():
    return Response('This is a really cool app', mimetype='text/plain')


@http.route('/plain-hello')
def plain_hello():
    return Response('Hello World!', mimetype='text/plain')


@http.route('/html-hello')
def html_hello():
    text = '''
    <html>
        <head>
        </head>
        <body>
            <h1>Hello World!</h1>
            <h2>Hello World!</h2>
            <h3>Hello World!</h3>
            <h4>Hello World!</h4>
        </body>
    </html>
    '''
    return Response(text, mimetype='text/html')


counter = 0


@http.route("/template")
def template():
    global counter
    counter = counter + 1
    message = "Hello, World " + str(counter)
    return render_template('template.html', message=message)


customers = [
    {
        'id': 1,
        'name': 'Bill Smith',
        'address': '123 Main St',
        'paid': False
    },
    {
        'id': 2,
        'name': 'Jane Jackson',
        'address': '1245 Birch Ave',
        'paid': True
    },
    {
        'id': 3,
        'name': 'Steve Stillwell',
        'address': '433 Peach Lane',
        'paid': True
    },
    {
        'id': 4,
        'name': 'Mary McKenna',
        'address': '3454 Apple St',
        'paid': False
    }
]


@http.route('/customers', methods=['GET'])
# @auth.login_required
def get_customers():
    print(jsonify({'customers': customers}))
    return jsonify({'customers': customers})


@http.route('/customers/<int:cust_id>', methods=['GET'])
def get_customer(cust_id):
    customer = [c for c in customers if c['id'] == cust_id]
    if len(customer) == 0:
        abort(404)
    return jsonify({'customer': customer[0]})


@http.route('/customer_query', methods=['GET'])
def query_customer():
    if not request.args or 'name' not in request.args:
        abort(400)
    matches = [c for c in customers if request.args['name'] in c['name']]
    if len(matches) == 0:
        abort(404)
    return jsonify({'customers': matches})


@http.route('/customers', methods=['POST'])
def create_customer():
    if not request.json or not 'name' in request.json:
        abort(400)
    customer = {
        'id': customers[-1]['id'] + 1,
        'name': request.json['name'],
        'address': request.json.get('address', ''),
        'paid': False
    }
    customers.append(customer)
    return jsonify({'customer': customer}), 201


def main():
    # Parse CLI args
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest=PORT, default=8080, help='HTTP port [8080]')
    parser.add_argument('-v', '--verbose', dest=LOG_LEVEL, default=logging.INFO, action='store_const',
                        const=logging.DEBUG, help='Enable debugging info')
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    port = int(os.environ.get('PORT', args[PORT]))
    logger.info("Starting customer server listening on port {}".format(port))

    http.run(debug=False, port=port, host='0.0.0.0')


if __name__ == "__main__":
    main()
