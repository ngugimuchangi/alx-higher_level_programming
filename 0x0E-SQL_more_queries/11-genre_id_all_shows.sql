-- Script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If  show doesn’t have a genre, display NULL
-- You can use only one SELECT statement

SELECT title, genre_id
FROM tv_shows ts
LEFT OUTER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
ORDER BY title ASC, genre_id ASC;
