Model: Default (GPT-3.5)

> select list of all tables from sqlite3 schema
> 
> 1 / 1

You can use the following SQL query to retrieve a list of all tables in a SQLite3 database:

sql

```sql
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;
```

This query selects the "name" column from the "sqlite\_master" table, which contains information about all the objects in the database schema. The "WHERE" clause filters the results to only include rows with a "type" of "table", and the "ORDER BY" clause sorts the results alphabetically by table name.

1 / 1