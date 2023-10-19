__lists all the cities of California that can be found in hbtn_0d_usa
__Results must be sorted in ascending order by cities.id
__You are not allowed to use the JOIN keyword

SELECT id, name
  FROM cities
 WHERE state_id = (SELECT id
       		     FROM states
		    WHERE name = "California")
 ORDER BY id;
