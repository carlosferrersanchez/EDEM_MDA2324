create view actor_view_adgp6 as
select actor_id, first_name, last_name
from actor
where first_name like 'C%';

select* 
from actor_view_adgp;

select actor_id, first_name, last_name
from actor_view_adg
where first_name in (select first_name from actor_view_adg where last_name like 'C%');

select language_id, title
from film
Where language_id in (select language_id from language where language_id = 1);

select *
from "language"
where language_id = 1;

select *
from film
where language_id != 1;

select c.first_name, a.address
from customer c
inner join address a on c.address_id = a.address_id
where address like '%A%';

select c.first_name, p.amount 
from customer c
inner join payment p on c.customer_id = p.customer_id
where payment >= 190;










