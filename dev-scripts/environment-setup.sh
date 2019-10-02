#!/bin/bash

sudo docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=benderquotes -v postgres:/var/lib/postgresql/data postgres
