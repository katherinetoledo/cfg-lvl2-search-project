import requests
import logging
from py_edamam import PyEdamam

# from py_edamam.exceptions import APIError, InvalidRecipeAPIKey

logger = logging.getLogger('PyEdamam')

def edamam(food):
    e = PyEdamam(recipes_appid = '24dca7f7', recipes_appkey = '41bb8956fc3d014759cc3f17edd941a5')
    for recipe in e.search_recipe(food):
        return recipe, recipe.url


def recipe_search(ingredient):
    #url = 'https://api.edamam.com/search?q={query}&app_id={id}&app_key={key}'.format(query=ingredient, id=recipes_appid, key=recipes_appkey)
    url = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    r = requests.get(url)
    if r.status_code == 401:
         logger.error('Invalid recipe API key')
         raise InvalidRecipeApiKey
    return r.json()

    r = r.json()
    if r.get("status") == "error":
        error = r.get("message")
        if not error:
            error = "Api request failed"
        logger.error(error)
        raise APIError
    return r

def build_recipe_query(api_key, cuisine):
    results = 'https://api.spoonacular.com/recipes/search?cuisine=' + cuisine + \
          "&apiKey=" + api_key + "&addRecipeInformation=True"
    r = requests.get(results)

    if r.status_code == 401:
        print("invalid recipe api key")
        raise Exception
    return r.json()

def run():
    ingredient = input('What ingredients would you like cooking?: ')
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print()


    with open ('recipes-list.txt', 'r') as recipes_file:
        recipes_list = recipes_file.read()
        recipes_list = recipes_list + ingredient + '' + recipe_search['recipe'] + recipe_search['label'] + recipe_search['url'] + '\n'

    with open ('recipes-list.txt', 'w+') as recipes_file:
        recipes_file.write(recipes_list)


run()