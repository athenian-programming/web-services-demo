# web-service-demos

```bash
http http://localhost:8080/plain-hello
```

```bash
http http://localhost:8080/html-hello
```

### Query all values
```bash
http http://localhost:8080/customers
```

### Query single value
```bash
http http://localhost:8080/customers/1
http http://localhost:8080/customers/2
http http://localhost:8080/customers/3
```


### Adding values via POST
```bash
http http://localhost:8080/customers name='Joe Jackson' 
http http://localhost:8080/customers
http http://localhost:8080/customers name='Jill West' address='456 Sycamore Lane'
http http://localhost:8080/customers
```