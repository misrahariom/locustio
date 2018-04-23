# locustio

This repository runs a locust io test on local customer repository.

Below is the url for customer api.

https://github.com/misrahariom/customer-api


Build  the docker images:

`docker build -t="hari-locallocustio" .`

Run the docker image:

`docker run --rm -v 'pwd':/locust -p 8089:8089 hari-locallocustio --host http://localhost:8080/ --no-web -c 100 -r 10`
