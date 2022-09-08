-- Script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If  show doesn’t have a genre, display NULL

SELECT title, name
FROM tv_shows ts
LEFT OUTER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
LEFT OUTER JOIN tv_genres tg
ON tsg.genre_id = tg.id
ORDER BY title ASC, name ASC;
