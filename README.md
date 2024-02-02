# Spread API

## Description

This Project helps you to get the spread for one or every markets present on BudaAPI

## Usage

The API Documentation is available in [this link](https://documenter.getpostman.com/view/16608319/2s9YyvBLJH).

## Run

Clone this repo and then run:

```console
foo@bar:~/buda.com-spread-api$ cd project
foo@bar:~/buda.com-spread-api/project$ docker-compose up
```

This will run the tests and then keep the server up.

## Considerations

- The base_url of the API is in localhost, considering that this is not a production environment project
- For the polling system, since the developer doesn´t know whether the current spread should be given or if it should be calculated by the system when the request is received, the polling endpoint supports both options: you can request the endpoint `spread/alert/<mid>` or you can pass the current spread as query_params `spread/alert/<mid>?spread=<value>`
