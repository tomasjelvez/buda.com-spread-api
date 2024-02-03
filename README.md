# Spread API

## Description

This Project helps you to get the spread for one or every market present on BudaAPI

## Usage

The API Documentation is available in [this link](https://documenter.getpostman.com/view/16608319/2s9YyvBLJH).

## Run

### With Docker

Make sure you have the port 8000 free.

Clone this repo and then run:

```console
foo@bar:~/buda.com-spread-api$ cd project
foo@bar:~/buda.com-spread-api/project$ docker-compose up
```

This will run the tests and then keep the server up.

### Local

Make sure you have the port 8000 free.

Clone this repo and then run:

```console
foo@bar:~/buda.com-spread-api$ cd project
foo@bar:~/buda.com-spread-api/project$ pip install -r requirements.txt
```

#### To run the tests

```console
foo@bar:~/buda.com-spread-api/project$ python manage.py test
```

#### To run the server

```console
foo@bar:~/buda.com-spread-api/project$ python manage.py runserver
```

## Considerations

- The base_url of the API is in localhost, considering that this is not a production environment project.
- We assumed that the current spread to be compared with the alert one needs to be calculated in real time when the request is made, so we used the previously made `get_market_spread` function.
- Considering that the polling system could hit an endpoint multiple times in a short period of time, we developed a json file "cache" system for the getting the alert spread. This way, we can eficiently read a file and access the value that we need to compare, instead of looking for it on a DataBase, which is the mainstream approach.
  params `spread/alert/<mid>`
- The tests made may not have full coverage over the system, but we intended to test a great part of it.
