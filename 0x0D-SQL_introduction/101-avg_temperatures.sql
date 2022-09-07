-- Script that displays the average temperature by city
-- sorted by temperature in descending order

SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
