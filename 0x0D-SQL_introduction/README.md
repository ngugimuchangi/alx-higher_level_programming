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
0. Script that lists all databases of your MySQL server.
	* [0-list_databases.sql](0-list_databases.sql)
1. Script that creates the database hbtn_0c_0 in your MySQL server.
	* If the database hbtn_0c_0 already exists, your script should not fail
	- [1-create_database_if_missing.sql](1-create_database_if_missing.sql)
2. Script that deletes the database hbtn_0c_0 in your MySQL server.
	* If the database hbtn_0c_0 doesn’t exist, your script should not fail
	- [2-remove_database.sql](2-remove_database.sql)0
3. Script that lists all the tables of a database in your MySQL server.
	* The database name should be passed as an argument of the mysql command
	- [3-list_tables.sql](3-list_tables.sql)
4. Script that creates a table called first_table in the current database in your MySQL server.

	* first_table description:
		- id INT
		- name VARCHAR(256)
	* If the table first_table already exists, your script should not fail
	* The database name should be passed as an argument of the mysql command
	* [4-first_table.sql](4-first_table.sql)
5. Script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
	* [5-full_table.sql](5-full_table.sql)
6. Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
	* All fields should be printed
	* The database name should be passed as an argument of the mysql command
	* [6-list_values.sql](6-list_values.sql)
7. Script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
	* New row:
		- id = 89
		- name = Best School
	* The database name should be passed as an argument of the mysql command
	* [7-insert_value.sql](7-insert_value.sql)
8. Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
	* The database name should be passed as an argument of the mysql command
	* [8-count_89.sql](8-count_89.sql)
9. Script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
	* second_table description:
		- id INT
		- name VARCHAR(256)
		- score INT
	* If the table second_table already exists, your script should not fail
	* The database name should be passed as an argument of the mysql command
	* The script should create these records:
		- id = 1, name = “John”, score = 10
		- id = 2, name = “Alex”, score = 3
		- id = 3, name = “Bob”, score = 14
		- id = 4, name = “George”, score = 8
	* [9-full_creation.sql](9-full_creation.sql)
10. Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

	* Results should display both the score and the name (in this order)
	* Records should be ordered by score (top first)
	* The database name should be passed as an argument of the mysql command
	* [10-top_score.sql](10-top_score.sql)
11. Script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
	* Results should display both the score and the name (in this order)
	* Records should be ordered by score (top first) 
	* The database name should be passed as an argument of the mysql command
	* [11-best_score.sql](11-best_score.sql)
12. Script that updates the score of Bob to 10 in the table second_table.
	* The database name should be passed as an argument of the mysql command
	* [12-no_cheating.sql](12-no_cheating.sql)
13. Script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
	* The database name should be passed as an argument of the mysql command
	* [13-change_class.sql](13-change_class.sql) 
14. Script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
	* The result column name should be average
	* The database name should be passed as an argument of the mysql command
	* [14-average.sql](14-average.sql)
15. Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

	* The result should display:
		- the score
		- the number of records for this score with the label number
	* The list should be sorted by the number of records (descending)
	* The database name should be passed as an argument of the mysql command
	* [15-groups.sql](15-groups.sql)
16. Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
	* Don’t list rows without a name value
	* Results should display the score and the name (in this order)
	* Records should be listed by descending score
	* The database name should be passed as an argument to the mysql command
	* [16-no_link.sql](16-no_link.sql)
17. Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
	* Cconverts all of the following to UTF8:
		- Database hbtn_0c_0
		- Table first_table
		- Field name in first_table
	* [100-move_to_utf8.sql](100-move_to_utf8.sql)
18. Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
	* [101-avg_temperatures.sql](101-avg_temperatures.sql)
19. Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
	* [102-top_city.sql](102-top_city.sql)
20. Script that displays the max temperature of each state (ordered by State name).
	* [103-max_state.sql](103-max_state.sql)
