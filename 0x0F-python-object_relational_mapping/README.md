# 0x0F. Python - Object-relational mapping

## About
* Connecting to MySQL database using Python DB API
* Abstraction of database operations using Object-Relational Mapping (0RM)
	* SQLAlchemy Basics

## Tasks
0. Script that lists all states from the database `hbtn_0e_0_usa`:
	* Take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
	* Uses the module MySQLdb (`import MySQLdb`)
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `states.id`
	* [0-select_states.py](0-select_states.py)
1. Script that lists all states with a name starting with N (upper N) from the database `hbtn_0e_0_usa`: 
	* Take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
	* Uses the module MySQLdb (`import MySQLdb`)
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `states.id`
	* [1-filter_states.py](1-filter_states.py)
2. Script that takes in an argument and displays all values in the states table of `hbtn_0e_0_usa` where name matches the argument:
	* Take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
	* Uses the module MySQLdb (`import MySQLdb`)
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `states.id`
	* [2-my_filter_states.py](2-my_filter_states.py)
3. Script that takes in arguments and displays all values in the states table of `hbtn_0e_0_usa` where name matches the argument and is safe from MySQL injections!
	* Take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
	* Uses the module MySQLdb (`import MySQLdb`)
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `states.id`
	* [3-my_safe_filter_states.py](3-my_safe_filter_states.py)
4. Script that lists all cities from the database `hbtn_0e_4_usa`
	* Take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
	* Uses the module MySQLdb (`import MySQLdb`)
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `cities.id`
	* [4-cities_by_state.py](4-cities_by_state.py)
5. Script that takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`
	* Take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (no argument validation needed)
	* Uses the module MySQLdb (`import MySQLdb`)
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `cities.id`
	* [5-filter_cities.py](5-filter_cities.py)
6. Python file that contains the class definition of a State and an instance `Base = declarative_base()`:
	* `State` class:
		* inherits from Base Tips
		* links to the MySQL table states
		* class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		* class attribute name that represents a column of a string with maximum 128 characters and can’t be null
	* [model_state.py](model_state.py)
7. Script that lists all State objects from the database `hbtn_0e_6_usa`
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connect to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `states.id`
	* [7-model_state_fetch_all.py](7-model_state_fetch_all.py)
8. Script that prints the first State object from the database `hbtn_0e_6_usa`
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connect to a MySQL server running on `localhost` at port `3306`
	* The state displayed must be the first in`states.id`
	* If the table `states` is empty, print `Nothing` followed by a new line
	* [8-model_state_fetch_first.py](8-model_state_fetch_first.py)
9. Script that lists all State objects that contain the letter `a` from the database `hbtn_0e_6_usa`
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connect to a MySQL server running on `localhost` at port `3306`
	* Results are sorted in ascending order by `states.id`
	* [9-model_state_filter_a.py](9-model_state_filter_a.py)
10. Script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
	* Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search`
	* Uses the module `SQLAlchemy`
	* Connect to a MySQL server running on `localhost` at port `3306`
	* Results display the `states.id`
	* If no `state` has the name searched for, displays `Not found`
	* [10-model_state_my_get.py](10-model_state_my_get.py)
11. Script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connect to a MySQL server running on `localhost` at port `3306`
	* Prints new `states.id` after creation
	* [11-model_state_insert.py](11-model_state_insert.py)
12. Script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connect to a MySQL server running on `localhost` at port `3306`
	* Changes the name of the `State` where `id = 2` to `New Mexico`
	* [12-model_state_update_id_2.py](12-model_state_update_id_2.py)
13. Script that deletes all `State` objects with `a` name containing the letter a from the database `hbtn_0e_6_usa`
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connect to a MySQL server running on `localhost` at port `3306`
	* [13-model_state_delete_a.py](13-model_state_delete_a.py)
14. Python file that contains the class definition of a `City`.
	* `City` class:
		* inherits from `Base` (imported from `model_state`)
		* links to the MySQL table `cities`
		* class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		* class attribute `name` that represents a column of a string of 128 characters and can’t be null
		* class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to states.id
	* Use the module `SQLAlchemy`
	* [model_city.py](model_city.py)
Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Results are display as follows (`<state name>`: (`<city id>`) `<city name>`)
	* [14-model_city_fetch_by_state.py](14-model_city_fetch_by_state.py)
15. Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`:
	* `City` class:
		* No change
	* State class:
		* In addition to previous requirements, the class attribute `cities` must represent a relationship with the class `City`. If the `State` object is deleted, all linked `City` objects must be automatically deleted. Also, the reference from a `City` object to his `State` should be named `state`
	* Use the module `SQLAlchemy`
	* [relationship_city.py](relationship_city.py), [relationship_state.py](relationship_state.py)
Write a script that creates the `State` “California” with the `City` “San Francisco” from the database `hbtn_0e_100_usa`: ([100-relationship_states_cities.py](100-relationship_states_cities.py))
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Uses `cities` relationship for all `State` objects
16. Script that lists all `State` objects, and corresponding `City` objects, contained in the database `hbtn_0e_101_usa`
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Uses `cities` relationship for all `State` objects
	* Results are sorted in ascending order by `states.id` and `cities.id`
	* [101-relationship_states_cities_list.py](101-relationship_states_cities_list.py)
17. Script that lists all `City` objects from the database `hbtn_0e_101_usa`
	* Takes 3 arguments: `mysql username`, `mysql password` and `database name`
	* Uses the module `SQLAlchemy`
	* Connects to a MySQL server running on `localhost` at port `3306`
	* Uses `state` relationship to access to the `State` object linked to the `City` object
	* Results are sorted in ascending order by `cities.id`
	* [102-relationship_cities_states_list.py](102-relationship_cities_states_list.py)
