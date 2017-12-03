# Web Servcies Demo

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Setup

Clone the repo with:
```bash
$ mkdir ~/git
$ cd git
$ git clone https://github.com/athenian-robotics/web-services-demo.git
```

Install the required python packages with:
```bash
$ cd ~/git/web-services-demo
$ pip install -r requirements.txt
```

Install [httpie](https://httpie.org) with:
```bash
$ brew install httpie
```

## Usage

Start the server with:
```bash
$ cd ~/git/web-services-demo
$ python customer_server.py
```

### CLI Calls

Say hello with:
```bash
$ http http://localhost:8080/plain-hello
$ http http://localhost:8080/html-hello
```

Query all customers with:
```bash
$ http http://localhost:8080/customers
```

Query customers by id with:
```bash
$ http http://localhost:8080/customers/1
$ http http://localhost:8080/customers/2
$ http http://localhost:8080/customers/3
```

Query customers by name with:
```bash
$ http http://localhost:8080/customer_query?name=Bill
```

Add values via POST with:
```bash
$ http http://localhost:8080/customers name='Joe Jackson' 
$ http http://localhost:8080/customers
$ http http://localhost:8080/customers name='Jill West' address='456 Sycamore Lane'
$ http http://localhost:8080/customers
```

### Programatic Calls

Query all customers with:
```bash
$ cd ~/git/web-services-demo
$ ./all_customers.py
```

Query customers by id with:
```bash
$ cd ~/git/web-services-demo
$ ./customer_by_id.py -i 1
$ ./customer_by_id.py -i 2
$ ./customer_by_id.py -i 3
```

Query customers by name with:
```bash
$ cd ~/git/web-services-demo
$ ./customer_by_name.py -n Bill
```

Create a new customer with:
```bash
$ cd ~/git/web-services-demo
$ ./create_customer.py -n "Mike Bryant" -a "1831 Dupont St"
```

