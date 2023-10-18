__a script that displays the average temperature (Fahrenheit) by city 
__ordered by temperature (descending order).

SELECT city,
AVG(value) as 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
