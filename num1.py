import os

# Задаём функции

def get_shop_list_by_dishes(dishesfd, person_count):
    for chek in dishesfd:
        if chek not in dishes.keys():
            return 'Блюдо не найдено!'
    resultdishes = {}
    for dish in dishes:
        if dish not in dishesfd:
            continue
        info = []
        for j in dishes[dish]:
            j['кл-во'] = int(j['кл-во']) * person_count
            info.append(j)
        resultdishes.setdefault(dish, info)
    return resultdishes

# Создадим словарь

with open("recipes.txt", "rt", encoding="utf-8") as f:
    dishes = {}
    for line in f:
        dish_name = line.strip()
        recipe_len = int(f.readline())
        ingredients = []
        for i in range(recipe_len):
            ing = f.readline().strip()
            prod, cnts, meas = ing.split(' | ')
            ingredients.append({
                'продукт': prod,
                'кл-во': cnts,
                'мера изм': meas
            })
        f.readline()
        dishes[dish_name] = ingredients

# print(dishes)

# Тестим метод

dishes_for_def = ['Омлет', 'Фахитос']
print(get_shop_list_by_dishes(dishes_for_def, 3))

