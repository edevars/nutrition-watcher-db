import requests
import lxml.html as html
import os
import datetime
from requests_html import HTMLSession

FOOD_SITE_URL = 'https://www.calories.info/'

XPATH_LINK_INGREDIENT_CATEGORIES = '//a[@class="calorie-link"]/@href'
XPATH_INGREDIENTS_NAME = '//tr[@class="kt-row even" or @class="kt-row odd"]/child::td[@class="food sorting_1"]/a/text()'
XPATH_INGREDIENTS_SERVING = '//tr[@class="kt-row even" or @class="kt-row odd"]/child::td[@class="serving portion"]/text()[1]'
INGREDIENT_GRAMS_PER_SERVING = '//tr[@class="kt-row even" or @class="kt-row odd"]/child::td[@class="serving portion"]/child::*/text()'
XPATH_INGREDIENTS_CALORIES = '//tr[@class="kt-row even" or @class="kt-row odd"]/child::td[@class="kcal portion"]/data/text()'
XPATH_CATEGORY_TITLE = 'concat(//h1/text(),"")'

CSV_HEADER = 'name, serving_quantity, grams_per_serving, cal\n'


def create_ingredient_file(link, today, OUTPUT_DIR, acum_file):
    print("Obtaining data from: ", link)
    try:
        session = HTMLSession()
        response = session.get(link)
        response.html.render()
        if response.status_code == 200:
            category = response.html.html
            parsed_category = html.fromstring(category)
            title = str(parsed_category.xpath(XPATH_CATEGORY_TITLE))

            with open(os.path.join(OUTPUT_DIR, f'{title}.csv'), 'w+', encoding='utf8') as file:
                file.write(CSV_HEADER)
                try:
                    ingredients_name_list = parsed_category.xpath(
                        XPATH_INGREDIENTS_NAME)
                    ingredients_serving_list = parsed_category.xpath(
                        XPATH_INGREDIENTS_SERVING)
                    ingredients_gram_per_serving = parsed_category.xpath(
                        INGREDIENT_GRAMS_PER_SERVING)
                    ingredients_calories_list = parsed_category.xpath(
                        XPATH_INGREDIENTS_CALORIES)

                    table_rows = len(ingredients_name_list)

                    for i in range(table_rows):
                        tmp_name = ingredients_name_list[i].replace(', ', '/')
                        tmp_ingredient_serving = ingredients_serving_list[i].replace(
                            ' (', '').replace(', ', '/')
                        info = f"{tmp_name}, {tmp_ingredient_serving}, {ingredients_gram_per_serving[i]}, {ingredients_calories_list[i]}\n"
                        file.write(info)
                        acum_file.write(info)

                except ValueError as ve:
                    print(ve)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(FOOD_SITE_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_categories = parsed.xpath(
                XPATH_LINK_INGREDIENT_CATEGORIES)

            today = datetime.date.today().strftime('%d-%m-%Y')
            OUTPUT_DIR = f'ingredients_scraped_{today}'
            if not os.path.isdir(today):
                os.mkdir(OUTPUT_DIR)

            print("Creating global Data Base for your convienence nwn")
            with open(os.path.join(
                    OUTPUT_DIR, 'GLOBAL_DATABASE.csv'), 'w+', encoding='utf8') as acum_file:
                acum_file.write(CSV_HEADER)
                for link in links_to_categories:
                    create_ingredient_file(link, today, OUTPUT_DIR, acum_file)

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == "__main__":
    run()
