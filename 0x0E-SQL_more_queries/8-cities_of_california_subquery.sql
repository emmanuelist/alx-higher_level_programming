-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
-- List all rows of a cloumn in a database
SELECT id,
    name
FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = 'California'
    )
ORDER BY id ASC;