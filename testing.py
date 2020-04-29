def get_ingredient():
    result = input("What do you have in the fridge today?")
    potential_ingredient = input(
        "Alright, is there anything else you would like to include on your ingredient list?(y/n)")
    if potential_ingredient == "y":
        additionals = input("What shall it be?")
        result == result + potential_ingredient
        print("Great, let's see what we can do with {} and {}!".format(result, additionals))
    else:
        print("Alright, looks like we can work with {}.".format(result))

    return result