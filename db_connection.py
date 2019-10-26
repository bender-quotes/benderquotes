import psycopg2

connection = psycopg2.connect(dbname="benderquotes",
                                user="postgres",
                                password="mysecretpassword",
                                host="127.0.0.1",
                                port="5432")
cursor = connection.cursor()
