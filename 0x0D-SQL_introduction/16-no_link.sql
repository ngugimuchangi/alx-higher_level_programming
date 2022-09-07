-- Display score and name if name is not null
-- Sort data in descending order based on score

SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC; 
