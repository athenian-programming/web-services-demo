import argparse
import logging
from threading import Thread

from flask import Flask
from flask import abort
from flask import jsonify
from flask import request

from utils import setup_logging
from utils import sleep

PORT = "port"
LOG_LEVEL = "loglevel"

if __name__ == "__main__":
    # Parse CLI args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", dest=PORT, default=8080, help="HTTP port [8080]")
    parser.add_argument("-v", "--verbose", dest=LOG_LEVEL, default=logging.INFO, action="store_const",
                        const=logging.DEBUG, help="Enable debugging info")
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    http = Flask(__name__)


    @http.route("/plain-hello")
    def plain_hello():
        return "Hello world"


    @http.route("/html-hello")
    def html_hello():
        return "<html><head></head><body><h1>Hello world</h1></body></html>"


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
        }
    ]


    @http.route("/customers")
    def get_customers():
        return jsonify({'customers': customers})


    @http.route("/customers/<int:cust_id>")
    def get_customer(cust_id):
        customer = [customer for customer in customers if customer['id'] == cust_id]
        if len(customer) == 0:
            abort(404)
        return jsonify({'customer': customer[0]})


    @http.route('/customers', methods=['POST'])
    def create_customer():
        if not request.json or not 'name' in request.json:
            abort(400)
        customer = {
            'id': customers[-1]['id'] + 1,
            'name': request.json['name'],
            'address': request.json.get('address', ""),
            'paid': False
        }
        customers.append(customer)
        return jsonify({'customer': customer}), 201


    # Run HTTP server in a thread
    Thread(target=http.run, kwargs={"port": args[PORT]}).start()

    sleep()
