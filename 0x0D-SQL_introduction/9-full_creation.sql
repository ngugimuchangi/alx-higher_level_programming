-- Create a table named second_table if it doesn't exist
-- Fields:
--	id (INT): person's id
--	name: person's name
--	score: person's score
-- Insert three records into the table

CREATE TABLE IF NOT EXISTS second_table
(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table VALUES (1, 'John', 10);
INSERT INTO second_table VALUES (2, 'Alex', 3);
INSERT INTO second_table VALUES (3, 'Bob', 14);
INSERT INTO second_table VALUES (4, 'George', 8);
