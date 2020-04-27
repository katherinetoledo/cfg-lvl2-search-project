import requests


def recipe_search(ingredient, diet):
    app_id = '24dca7f7'
    app_key = '41bb8956fc3d014759cc3f17edd941a5'
    result = requests.get(
        'https://api.edamam.com/search?q={}&diet={}&app_id={}&app_key={}'.format(ingredient, diet, app_id, app_key))
    data = result.json()
    return data['hits']


def get_ingredient():
    result = input('What ingredient would you like to cook?:')
    return result


def get_diet():
    done = False
    while not done:
        print('What kind of diet are you on?\n'
              'balanced\n'
              'high protein\n'
              'high-fiber\n'
              'low-fat\n'
              'low-carb\n'
              'low-sodium\n')
        diet = input('Type one of the options: ')
        if diet != 'balanced' and diet != 'high protein' and diet != 'high-fiber' and diet != 'low-fat' and diet != 'low-carb' and diet != 'low-sodium':
            print('Try again.')
        else:
            done = True

    result = diet
    if diet == '1':
        result = 'balanced'
    elif result == '2':
        result = 'high-protein'
    elif diet == '3':
        result = 'high-fiber'
    elif diet == '4':
        result = 'low-fat'
    elif diet == '5':
        result = 'low-carb'
    elif diet == '6':
        result = 'low-sodium'

    return result


def run():
    ingredient = get_ingredient()
    diet = get_diet()
    results = recipe_search(ingredient, diet)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])

    with open('recipes_list.txt', 'r') as recipes_file:
        recipes_list = recipes_file.read()
        recipes_list += ingredient
        for result in results:
            recipe = result['recipe']
            recipes_list = recipes_list + '\n' + recipe['label'] + '\n' + recipe['url'] + '\n'

    with open('recipes_list.txt', 'w+') as recipes_file:
        recipes_file.write(recipes_list)


run()