[![Run on Repl.it](https://repl.it/badge/github/athenian-programming/web-services-demo)](https://repl.it/github/athenian-programming/web-services-demo)

# Web Services Demo

## Related Posts
* [How to make REST Api in Python](https://repl.it/talk/learn/How-to-make-Rest-Api-in-Python/9038)

## Setup

Clone the repo with:
```bash
mkdir ~/git
cd git
git clone https://github.com/athenian-robotics/web-services-demo.git
```

Install [httpie](https://httpie.org) with:
```bash
brew install httpie
```

Install the required python packages with:
```bash
cd ~/git/web-services-demo
pip install -r requirements.txt
```

## Running the server

### Local 

Start the server with:
```bash
cd ~/git/web-services-demo
python src/customer_server.py
```

### Ngrok 

Install [ngrok](https://ngrok.com) with:
```bash
brew cask install ngrok
```

Launch `ngrok` with:
```bash
ngrok http 8080
```
 
### Deploying to repl.it
 [![Run on Repl.it](https://repl.it/badge/github/athenian-programming/web-services-demo)](https://repl.it/github/athenian-programming/web-services-demo)


### Deploying to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1) Create a new Heroku app with:
```
heroku create [APP_NAME]
```

2) Deploy code to Heroku with:
```
git push heroku master
```

3) Open Heroku app in browser with:
```
heroku open
```
or visit [http://APP_NAME.herokuapp.com](http://APP_NAME.herokuapp.com).

4) View server logs with the `heroku logs` command with:
```
heroku logs --tail
```

## CLI Calls

Say hello with:
```bash
http :8080/plain-hello
http :8080/html-hello
```

Query all customers with:
```bash
http :8080/customers
```

Query customers by id with:
```bash
http :8080/customers/1
http :8080/customers/2
http :8080/customers/3
```

Query customers by name with:
```bash
http :8080/customer_query?name=Bill
```

Add values via POST with:
```bash
http :8080/customers name='Joe Jackson' 
http :8080/customers
http :8080/customers name='Jill West' address='456 Sycamore Lane'
http :8080/customers
```

### Programatic Calls

Query all customers with:
```bash
cd ~/git/web-services-demo
src/all_customers.py
```

Query customers by id with:
```bash
cd ~/git/web-services-demo
src/customer_by_id.py -i 1
src/customer_by_id.py -i 2
src/customer_by_id.py -i 3
```

Query customers by name with:
```bash
cd ~/git/web-services-demo
src/customer_by_name.py -n Bill
```

Create a new customer with:
```bash
cd ~/git/web-services-demo
src/create_customer.py -n "Mike Bryant" -a "1831 Dupont St"
```