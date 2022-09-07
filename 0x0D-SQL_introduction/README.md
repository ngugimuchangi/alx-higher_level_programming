# 0x0D. SQL - Introduction
## About
Database introduction
Structured Query Language Introduction
* Data definition language (DDL)
* Data manipulation language (DML)
* SQL basic operations: `CREATE`, `ALTER`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`
* Subqueries
* SQL functions
### Tasks
0. Write a script that lists all databases of your MySQL server.
	* [0-list_databases.sql](0-list_databases.sql)
1. Write a script that creates the database hbtn_0c_0 in your MySQL server.
	* If the database hbtn_0c_0 already exists, your script should not fail
	* You are not allowed to use the SELECT or SHOW statements
	- [1-create_database_if_missing.sql](1-create_database_if_missing.sql)
2. Write a script that deletes the database hbtn_0c_0 in your MySQL server.
	* If the database hbtn_0c_0 doesn’t exist, your script should not fail
	* You are not allowed to use the SELECT or SHOW statements
	- [2-remove_database.sql](2-remove_database.sql)0
3. Write a script that lists all the tables of a database in your MySQL server.
	* The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)
	- [3-list_tables.sql](3-list_tables.sql)
4. Write a script that creates a table called first_table in the current database in your MySQL server.

	* first_table description:
	- id INT
	- name VARCHAR(256)

	* The database name will be passed as an argument of the mysql command
	* If the table first_table already exists, your script should not fail
	* You are not allowed to use the SELECT or SHOW statements
