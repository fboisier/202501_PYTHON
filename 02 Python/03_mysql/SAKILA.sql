/* 1.- ¿Qué consulta ejecutarías para obtener todos los clientes (customer)
        dentro de la ciudad ‘Santiago de los Caballeros’? Tu consulta debe
        devolver el nombre, apellido, correo electrónico y dirección del cliente. 
*/
SELECT 
    c.first_name, c.last_name, c.email, a.address
FROM
    customer c
        JOIN
    address a ON c.address_id = a.address_id
        JOIN
    city ci ON a.city_id = ci.city_id
WHERE
    ci.city = 'Santiago de los Caballeros';
    
/* 
2
¿Qué consulta ejecutarías para obtener todas las películas de categoría Sci-Fi? 
Tu consulta debe devolver el título de la película, la descripción, el año de lanzamiento,
la clasificación, las características especiales y el género (categoría).
*/
SELECT 
    film.title, 
    film.description, 
    film.release_year, 
    film.rating, 
    film.special_features, 
    category.name 
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Sci-Fi';

/*
3
¿Qué consulta ejecutarías para obtener todas las películas
en las que aparece la actriz ‘WHOOPI’? Tu consulta debe devolver
el id del actor, el nombre del actor, el título de la película,
la descripción y el año de lanzamiento.
*/

SELECT a.actor_id, a.first_name, a.last_name, f.title, f.description, f.release_year
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE a.first_name = 'WHOOPI';

/*
4
¿Qué consulta ejecutarías para obtener todos los clientes de store_id=1
y dentro de estas ciudades (1, 42, 312 y 459)? Tu consulta debe devolver
el nombre, apellido, correo electrónico y dirección del cliente.
*/

SELECT 
    customer.first_name,       
    customer.last_name,         
    customer.email,          
    address.address            
FROM customer
INNER JOIN address ON customer.address_id = address.address_id
INNER JOIN city ON address.city_id = city.city_id  
WHERE customer.store_id = 1        
AND city.city_id IN (1, 42, 312, 459);

/*
5
¿Qué consulta ejecutarías para obtener todas las películas con rating = ‘PG-13’,
que como característica especial (special_feature) incluya ‘trailers’, y
unidas por actor_id = 23?  Tu consulta debe devolver el título de la película,
la descripción, el año de lanzamiento, la clasificación y la característica
especial. Sugerencia: puede usar la función LIKE y “%%” para la búsqueda de special_feature.
*/

SELECT 
     f.title, f.description, f.release_year, f.rating, f.special_features
FROM
    film f
        JOIN
    film_actor fa ON f.film_id = fa.film_id
WHERE
    f.rating = 'PG-13'
        AND f.special_features LIKE '%trailers%'
        AND fa.actor_id = 23;

/*
6
¿Qué consulta ejecutarías para obtener todos los actores que se participaron en 
film_id = 157? Tu consulta debe devolver film_id, título, actor_id y actor_name.
*/


SELECT 
     f.film_id, f.title, a.actor_id, a.first_name, a.last_name
FROM
    actor a
        JOIN
    film_actor fa ON a.actor_id = fa.actor_id
    JOIN
    film f ON f.film_id = fa.film_id
    WHERE f.film_id = 157;
    

/*
7
¿Qué consulta ejecutarías para obtener todas las películas de categoría ‘Horror’ 
con costo de renta de .99 (rental_rate)? Tu consulta debe devolver el título de la 
película, la descripción, el año de lanzamiento, la clasificación, las 
características especiales y el género (categoría).
*/

SELECT 
    f.title, f.description, f.release_year, f.rating, f.special_features, c.name as categoria
FROM
    film f
        JOIN
    film_category fc ON f.film_id = fc.film_id
        JOIN
    category c ON c.category_id = fc.category_id
WHERE
    c.name = 'Horror'
        AND f.rental_rate = 0.99;

/*
8
¿Qué consulta ejecutarías para obtener todas las películas de categoría musical 
(Music) en las que haya participado VAL BOLGER? Tu consulta debe devolver el título 
de la película, la descripción, el año de lanzamiento, la clasificación, las 
características especiales, el género (categoría) y el nombre y apellido del actor.
*/


SELECT 
    f.title, f.description, f.release_year, f.rating, f.special_features, c.name as categoria, CONCAT(a.first_name, ' ', a.last_name) as actor
FROM
    film f
        JOIN
    film_category fc ON f.film_id = fc.film_id
        JOIN
    category c ON c.category_id = fc.category_id
    JOIN
    film_actor fa ON fa.film_id = f.film_id 
    JOIN 
    actor a ON a.actor_id = fa.actor_id
    WHERE c.name = 'Music' AND CONCAT(a.first_name, ' ', a.last_name) = 'VAL BOLGER'