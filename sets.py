from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    empty_set = set()
    for i in dish_ingredients:
        empty_set.add(i)
    return dish_name, empty_set


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    list=[]
    for a in ALCOHOLS:
        list.append(a)
    
        
    for i, alc in enumerate(list):
        if list[i] in drink_ingredients:
            break
    if list[i] in drink_ingredients:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"

            
        
         






