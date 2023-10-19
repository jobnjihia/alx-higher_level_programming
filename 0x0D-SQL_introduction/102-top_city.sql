__script that displays the top 3 of cities temperature during July and August 
__ordered by temperature (descending)

SELECT city,
AVG(value) as 'avg_temp'
FROM tempuratures
WHERE month = 7 OR month = 8
GROUP BY city
ORDERED BY avg_temp DESC
LIMIT 3;