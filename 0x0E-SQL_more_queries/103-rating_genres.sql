-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating

SELECT name, SUM(rate) AS rating
FROM tv_genres tg
LEFT OUTER JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
LEFT OUTER JOIN tv_show_ratings tsr
ON tsg.show_id = tsr.show_id
GROUP BY name
ORDER BY rating DESC;
