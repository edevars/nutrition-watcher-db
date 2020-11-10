create schema nutrition_watcher default character set 'utf8mb4';

use nutrition_watcher;

create table users (
  user_id int not null auto_increment,
  user_name VARCHAR(100) NOT NULL,
  user_url_photo VARCHAR(255) NULL,
  email VARCHAR(150) NOT NULL,
  user_password VARCHAR(255) NOT NULL,
  primary key (user_id),
  unique (email)
);
  
create table daily_checks(
	id_daily_check int not null auto_increment,
    weight int not null,
    waist_lenght int not null,
    date_check date not null,
    water_glasses int,
    calories_count int not null,
    user_id int not null,
    primary key(id_daily_check),
    foreign key (user_id) references users(user_id)
);

create table recipes(
	recipe_id int not null auto_increment,
    calories int not null,
    url_photo varchar(255),
    primary key (recipe_id)
);

create table daily_checks_recipes(
	dcr_id int not null auto_increment,
    id_daily_check int not null,
    recipe_id int not null,
    primary key (dcr_id),
    foreign key (id_daily_check) references daily_checks(id_daily_check),
    foreign key (recipe_id) references recipes(recipe_id)
);

create table steps(
	steps_id int not null auto_increment,
    order_no int not null,
    description_step text not null,
    recipe_id int not null,
    primary key (steps_id), 
    foreign key (recipe_id) references recipes(recipe_id)
);


create table ingredients(
	ingredient_id int not null auto_increment,
    ingredient_name varchar(255) not null,
    total_calories int not null,
    measure varchar(20) not null,
    primary key (ingredient_id)
);

create table recipes_ingredients(
	ri_id int not null auto_increment,
    recipe_id int not null,
    ingredient_id int not null,
    primary key (ri_id),
    foreign key (recipe_id) references recipes(recipe_id),
    foreign key (ingredient_id) references ingredients(ingredient_id)
);
