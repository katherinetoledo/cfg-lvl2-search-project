import requests

def recipe_search(ingredient):
    app_id = '66251a7b'
    app_key = 'd4a212e9627ea62610fc7ce07eb8f34c'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('What ingredients would you like cooking? ')
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print(recipe['healthLabels'])
        print('Calories: ' + str(round(recipe['calories']))+ ' kcal')
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