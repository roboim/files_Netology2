# Чтение файла recipes.txt
from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count):
    """
    Ingredients counting
    """
    dishes_book = read_dishes_book()
    set_of_ingredients = {
        # 'ingredient_name':{'measure': '', 'quantity': 0}
    }
    for dish in dishes:
        for ingredient in dishes_book[dish]:
            if ingredient['ingredient_name'] in set_of_ingredients.keys():
                set_of_ingredients[ingredient['ingredient_name']]['quantity'] += \
                    int(ingredient['quantity']) * person_count
            else:
                set_of_ingredients.setdefault(ingredient['ingredient_name'],
                                              {'measure': ingredient['measure'], 'quantity': ingredient['quantity']})
                set_of_ingredients[ingredient['ingredient_name']]['measure'] = ingredient['measure']
                set_of_ingredients[ingredient['ingredient_name']]['quantity'] = \
                    int(ingredient['quantity']) * person_count
    pprint(set_of_ingredients, sort_dicts=True)


def read_dishes_book():
    """
    Read recipes.txt
    """
    with open("recipes.txt", "r", encoding="UTF-8") as job_file:
        dishes_book = {}
        for line in job_file:
            dish = line.strip()
            ingredients_n = int(job_file.readline())
            ingredients = []
            for _ in range(ingredients_n):
                string_ingredient = job_file.readline()
                string_ingredient = string_ingredient.strip()
                ingredient_name, quantity, measure = string_ingredient.split(" | ")
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(ingredient)
            job_file.readline()
            dishes_book[dish] = ingredients
    return dishes_book


# help(get_shop_list_by_dishes)
# help(read_dishes_book)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
