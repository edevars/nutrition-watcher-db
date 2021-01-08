CREATE DATABASE nutrition_watcher 
WITH 
-- put OWNER=postgres as default
OWNER =  
encoding = 'UTF8';

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  user_name VARCHAR(100) NOT NULL,
  user_url_photo VARCHAR(255) NULL,
  email VARCHAR(150) NOT NULL,
  user_password VARCHAR(255) NOT NULL,
  UNIQUE (email)
);
  
CREATE TABLE daily_checks(
	id_daily_check SERIAL PRIMARY KEY,
    weight INT NOT NULL,
    waist_lenght INT NOT NULL,
    date_check date not null,
    water_glasses int,
    calories_count INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE recipes(
	recipe_id SERIAL PRIMARY KEY,
    calories INT NOT NULL,
    url_photo varchar(255)
);

CREATE TABLE daily_checks_recipes(
	dcr_id SERIAL PRIMARY KEY,
    id_daily_check INT NOT NULL,
    recipe_id INT NOT NULL,
    FOREIGN KEY (id_daily_check) REFERENCES daily_checks(id_daily_check),
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id)
);

CREATE TABLE steps(
	steps_id SERIAL PRIMARY KEY,
    order_no INT NOT NULL,
    description_step text not null,
    recipe_id INT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id)
);


CREATE TABLE ingredients(
	ingredient_id SERIAL PRIMARY KEY,
    ingredient_name varchar(255) not null,
    total_calories INT NOT NULL,
    measure varchar(30) not null,
    grams_per_measure VARCHAR(20)
);

CREATE TABLE recipes_ingredients(
	ri_id SERIAL PRIMARY KEY,
    recipe_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
);
