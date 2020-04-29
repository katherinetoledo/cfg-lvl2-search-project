import requests

def recipe_search(ingredient, diet):
    app_id = '24dca7f7'
    app_key = '41bb8956fc3d014759cc3f17edd941a5'
    result = requests.get(
        'https://api.edamam.com/search?q={}&diet={}&app_id={}&app_key={}'.format(ingredient, diet, app_id, app_key))
    data = result.json()
    return data['hits']


def get_ingredient():
    result = input("What do you have in the fridge/cupboard today? ")
    potential_ingredient = input(
        "Alright, is there anything else you would like to include on your ingredient list?(y/n)")
    if potential_ingredient == "y":
        additionals = input("What shall it be?")
        result == result + potential_ingredient
        print("Great, let's see what we can do with {} and {}!".format(result, additionals))
    else:
        print("Alright, looks like we can work with {}.".format(result))
    return result


def get_diet():
    done = False
    while not done:
        print('What kind of diet are you on?\n'
              'balanced\n'
              'high-protein\n'
              'high-fiber\n'
              'low-fat\n'
              'low-carb\n'
              'low-sodium\n')
        diet = input('Type one of the options: ')
        if diet != 'balanced' and diet != 'high-protein' and diet != 'high-fiber' and diet != 'low-fat' and diet != 'low-carb' and diet != 'low-sodium':
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
        print('Name: ' + recipe['label'])
        print('URL: ' + recipe['url'])
        print('Health Labels: ' + str(recipe['healthLabels']))
        print('Calories: ' + str(round(recipe['calories'])) + ' kcal')
        print()

    with open('recipes_list.txt', 'a') as recipes_file:
        recipes_file.write('\nRecipe Search\n')

    with open('recipes_list.txt', 'r') as recipes_file:
        recipes_list = recipes_file.read()
        recipes_list += 'Ingredient: ' + ingredient + '\n' + 'Diet: ' + diet + '\n'
        for result in results:
            recipe = result['recipe']
            recipes_list = recipes_list + '\n' + recipe['label'] + '\n' + recipe['url'] + '\n' + " ".join(recipe['healthLabels']) + '\n' + 'Calories: ' + str(round(recipe['calories'])) + ' kcal' + '\n\n'
            recipes_file.write

    with open('recipes_list.txt', 'w+') as recipes_file:
        recipes_file.write(recipes_list)

    with open('recipes_list.txt', 'a') as recipes_file:
        recipes_file.write('\nEnjoy :)\n')


run()

