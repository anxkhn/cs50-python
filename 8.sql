-- SQL query that lists the names of the songs that feature other artists.
SELECT name FROM songs WHERE artist_id = (SELECT name FROM artists WHERE name = '.feat');