# Web Servcies Demo

## Setup

Clone the repo with:
```bash
$ mkdir ~/git
$ cd git
$ git clone https://github.com/athenian-robotics/web-services-demo.git
```

Install the required python modules with:
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

Query all values with:
```bash
$ http http://localhost:8080/customers
```

Query single value with:
```bash
$ http http://localhost:8080/customers/1
$ http http://localhost:8080/customers/2
$ http http://localhost:8080/customers/3
```


Add values via POST with:
```bash
$ http http://localhost:8080/customers name='Joe Jackson' 
$ http http://localhost:8080/customers
$ http http://localhost:8080/customers name='Jill West' address='456 Sycamore Lane'
$ http http://localhost:8080/customers
```