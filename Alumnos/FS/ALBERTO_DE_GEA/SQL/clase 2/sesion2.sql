select country_id, country from country;
-- sql prueba --

select title, rental_rate, replacement_cost from film;

select rating ,
count(distinct film_id) as total_peliculas,
avg(rental_rate) as precio_medio,
max(rental_rate) as mas_cara,
min(rental_rate) as mas_barata,
avg(length) as media_duracion,
min(extract(year from last_update)) as min_año,
max(extract(year from last_update)) as max_año
from film
group by rating;


select rating, 
count(distinct film_id) as total_pelis
from film
group by rating
having count(distinct film_id) > 200;



select rating, 
avg(rental_rate)
from film
group by rating
having avg(rental_rate) > 3;


select rating, 
avg(length)
from film
group by rating
having avg(length) > 115;