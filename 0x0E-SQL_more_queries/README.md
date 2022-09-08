# 0x0E. SQL - More queries
## About
* Creating users
* Granting permissions
* SQL constraints
* Joining tables in queries
* Union and minus
## Tasks
0. Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
	* [0-privileges.sql](0-privileges.sql)
1. Script that creates the MySQL server user user_0d_1.
	* User_0d_1 should have all privileges on your MySQL server
	* The user_0d_1 password should be set to user_0d_1_pwd
	* [1-create_user.sql](1-create_user.sql)
2. Script that creates the database hbtn_0d_2 and the user user_0d_2.
	* user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
	* The user_0d_2 password should be set to user_0d_2_pwd
	* [2-create_read_user.sql](2-create_read_user.sql)
3. Script that creates the table force_name on your MySQL server.
	* force_name description:
		- id INT
		- name VARCHAR(256) can’t be null
	* [3-force_name.sql](3-force_name.sql)
4. Script that creates the table id_not_null on your MySQL server.
	* id_not_null description:
		- id INT with the default value 1
		- name VARCHAR(256)
	* [4-never_empty.sql](4-never_empty.sql)
5. Script that creates the table unique_id on your MySQL server.
	* unique_id description:
		- id INT with the default value 1 and must be unique
		- name VARCHAR(256)
	* [5-unique_id.sql](5-unique_id.sql)
6. Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
	* states description:
		- id INT unique, auto generated, can’t be null and is a primary key
		- name VARCHAR(256) can’t be null
	* [6-states.sql](6-states.sql)
7. Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
	* cities description:
		- id INT unique, auto generated, can’t be null and is a primary key
		- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
		- name VARCHAR(256) can’t be null
	* [7-cities.sql](7-cities.sql)
8. Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
	* The states table contains only one record where name = California (but the id can be different, as per the example)
	* Results must be sorted in ascending order by cities.id
	* [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql)
9. Script that lists all cities contained in the database hbtn_0d_usa.
	* Each record should display: cities.id - cities.name - states.name
	* Results must be sorted in ascending order by cities.id
	* [9-cities_by_state_join.sql](9-cities_by_state_join.sql)
10. Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
	* Each record should display: tv_shows.title - tv_show_genres.genre_id
	* Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
	* [10-genre_id_by_show.sql](10-genre_id_by_show.sql)
11. Script that lists all shows contained in the database hbtn_0d_tvshows.
	* Each record should display: tv_shows.title - tv_show_genres.genre_id
	* Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
	* If a show doesn’t have a genre, display NULL
	* [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql)
12. Script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
	* Each record should display: tv_shows.title - tv_show_genres.genre_id
	* Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
	* You can use only one SELECT statement
	* [12-no_genre.sql](12-no_genre.sql)
13. Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
	* Each record should display: <TV Show genre> - <Number of shows linked to this genre>
	* First column must be called genre
	* Second column must be called number_of_shows
	* Don’t display a genre that doesn’t have any shows linked
	* Results must be sorted in descending order by the number of shows linked
	* [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql)
14. Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
	* The tv_shows table contains only one record where title = Dexter (but the id can be different)
	* Each record should display: tv_genres.name
	* Results must be sorted in ascending order by the genre name
	* [14-my_genres.sql](14-my_genres.sql)
15. Script that lists all Comedy shows in the database hbtn_0d_tvshows.
	* The tv_genres table contains only one record where name = Comedy (but the id can be different)
	* Each record should display: tv_shows.title
	* Results must be sorted in ascending order by the show title
	* [15-comedy_only.sql](15-comedy_only.sql)
16. Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
	* If a show doesn’t have a genre, display NULL in the genre column
	* Each record should display: tv_shows.title - tv_genres.name
	* Results must be sorted in ascending order by the show title and genre name
	* You can use only one SELECT statement
	* [16-shows_by_genre.sql](16-shows_by_genre.sql)
17. Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
	* The tv_shows table contains only one record where title = Dexter (but the id can be different)
	* Each record should display: tv_genres.name
	* Results must be sorted in ascending order by the genre name
	* [100-not_my_genres.sql](100-not_my_genres.sql)
18. Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
	* The tv_genres table contains only one record where name = Comedy (but the id can be different)
	* Each record should display: tv_shows.title
	* Results must be sorted in ascending order by the show title
	* [101-not_a_comedy.sql](101-not_a_comedy.sql)
19. Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
	* Each record should display: tv_shows.title - rating sum
	* Results must be sorted in descending order by the rating
	* [102-rating_shows.sql](102-rating_shows.sql)
20. Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
	* Each record should display: tv_genres.name - rating sum
	* Results must be sorted in descending order by their rating
	* [103-rating_genres.sql](103-rating_genres.sql)
