-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT title FROM tv_shows
WHERE title NOT IN
(SELECT title FROM tv_shows ts
INNER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
INNER JOIN tv_genres tg
ON tsg.genre_id = tg.id
WHERE name = 'Comedy')
ORDER BY title ASC;
