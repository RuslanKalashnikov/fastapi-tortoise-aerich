## STARTUP
#### `docker-compose up`

### ONLY ONE TIME

1) Init aerich: </br>
    `docker-compose exec toerich aerich init -t database.DATABASE_CONFIG`
    </br>
    #### CORRECT ANSWER:
    ```
    * created '/migrations' 
    * created 'aerich.ini'
    ```
2) Init aerich and all tortoise models. </br>
    `docker-compose exec toerich aerich init-db`
    </br>
    #### CORRECT ANSWER:
    ```
    * Success create app migrate location migrations/models
    * Success generate schema for app "models"
    ```

### On any tortoise model change

1) Makemigration </br>
    `docker-compose exec toerich aerich migrate --name add_surname`
    </br>
    #### CORRECT ANSWER:
    ```
    * Success migrate 1_20220503102224_add_surname.sql
    ```

2) Apply </br>
    `docker-compose exec toerich aerich upgrade`
    <br>
    #### CORRECT ANSWER:
    ```
    * Success upgrade 1_20220503102224_add_surname.sql
   ```

3) Rollback </br>
    `docker-compose exec toerich aerich downgrade`
    <br>
    #### CORRECT ANSWER:
    ```
    * Success downgrade 1_20220503102224_add_surname.sql
   ```
