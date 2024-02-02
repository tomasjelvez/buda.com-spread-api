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
- The endpoint designed for do the polling operation supports both options: you can request the endpoint `spread/alert/<mid>` so the system calculates the current spread on its own, or you can pass the current spread as query_params `spread/alert/<mid>?spread=<value>`
- Considering that the polling system could hit an endpoint multiple times in a short period of time, we developed a json file "cache" system for the getting the alert spread. This way, we can eficiently read a file and access the value that we need to compare, instead of looking for it on a DataBase, which is the mainstream approach.
