gitimport requests

def recipe_search(ingredient):
    app_id = '24dca7f7'
    app_key = '41bb8956fc3d014759cc3f17edd941a5'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('What ingredients would you like cooking?: ')
    results = recipe_search(ingredient)

    with open('recipes-list.txt', 'r') as recipes_file:
        recipes_list = recipes_file.read()
        recipes_list = recipes_list + ingredient + '' + recipe_search['recipe'] + \
                       recipe_search['label'] + recipe_search['url'] + '\n'

    with open('recipes_list.txt', 'w+') as recipes_file:
        recipes_file.write(recipes_list)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print()

run ()



