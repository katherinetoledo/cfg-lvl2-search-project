import requests

def recipe_search(ingredient):
    app_id = '24dca7f7'
    app_key = '41bb8956fc3d014759cc3f17edd941a5'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('What ingredients would you like cooking?: ')
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print()


    with open('recipes_list.txt', 'r') as recipes_file:
        recipes_list = recipes_file.read()
        recipes_list += ingredient
        for result in results:
            recipe = result['recipe']
            recipes_list = recipes_list + '\n' + recipe['label'] + '\n' + recipe['url'] + '\n'

    with open('recipes_list.txt', 'w+') as recipes_file:
        recipes_file.write(recipes_list)



run ()

