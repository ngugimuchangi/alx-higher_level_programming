-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT title
FROM tv_shows as ts
LEFT OUTER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
LEFT OUTER JOIN tv_genres tg
ON tsg.genre_id = tg.id
WHERE name = 'Comedy'
ORDER BY title ASC;
