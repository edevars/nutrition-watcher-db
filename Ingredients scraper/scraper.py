import requests
import lxml.html as html

FOOD_SITE_URL = 'https://www.calories.info/'

XPATH_LINK_INGREDIENT_CATEGORIE = '//a[@class="calorie-link"]/@href'
XPATH_INGREDIENT_NAME = '//tr[@class="kt-row even" or @class="kt-row odd"]/child::td[@class="food sorting_1"]/a/text()'
XPATH_INGREDIENT_SERVING = '//tr[@class="kt-row even" or @class="kt-row odd"]/child::td[@class="serving portion"]/text()'
XPATH_INGREDIENT_CALORIES = '//tr[@class="kt-row even" or @class="kt-row odd"]/child::td[@class="kcal portion"]/data/text()'


def parse_home():
    try:
        response = requests.get(FOOD_SITE_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_categories = parsed.xpath(XPATH_LINK_INGREDIENT_CATEGORIE)
            print(links_to_categories)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == "__main__":
    run()
