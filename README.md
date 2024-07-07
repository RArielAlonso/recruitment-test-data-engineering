# Recruitment Data Engineer

## Start building images

1- Command to build images from docker compose

`docker compose build `

2- Command to start database

`docker compose up database`

3- Wait till database is on and if you want to access database to see schema, the password will be asked or you can run adminer in 

- By CLI

    `docker exec -it db-test mysql -ucodetest  -p`

- By Adminder

    ```docker compose up admin```

    Go the browser and type in http://localhost:8080

4- Run the ETL container to load data to the database

`docker compose run --rm etl-python` 

5- Run the Output container to write the summary as a json file

`docker compose run --rm output-python`

## Considerations

- No persist data from database, it could be set up by a volume

```
volumes: 
    - mysql-data:/var/lib/mysql
```

- Enviroment managed with poetry (https://python-poetry.org/)

To setup enviroment files and packages used within containers, I've decided to use poetry.

- Schema of the database

Set up the primary key as an integer to reduce the amount of spaced used, and created a similar schema of a DW.

`people as Fact table`

`places as a Dim Table`

![Schema](/files/schema.png)


- The process is not written to increment data as a batch process, as the task doesn't requeried to be incremental.

