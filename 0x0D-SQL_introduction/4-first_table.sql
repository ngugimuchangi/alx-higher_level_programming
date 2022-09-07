-- Create a table named first_table if it doesn't exist
-- Fields:
-- 	id: an integer
--	name: string of variable character lenght upto max 256 characters

CREATE TABLE IF NOT EXISTS first_table
(id INT, name VARCHAR(256));
