T = int(input())
for t in range(T):
    N = int(input())
    foreign_ingredient_pizzas = dict()
    native_ingredient_pizzas = dict()

    for _ in range(N):
        pizza_name = input().strip()

        foreign_line = input().split()
        foreign_ingredients = foreign_line[1:]

        native_line = input().split()
        native_ingredients = native_line[1:]

        for f_ing in foreign_ingredients:
            if f_ing not in foreign_ingredient_pizzas:
                foreign_ingredient_pizzas[f_ing] = set()
            foreign_ingredient_pizzas[f_ing].add(pizza_name)

        for n_ing in native_ingredients:
            if n_ing not in native_ingredient_pizzas:
                native_ingredient_pizzas[n_ing] = set()
            native_ingredient_pizzas[n_ing].add(pizza_name)

    possible_translations = []
    for f_ing, f_pizzas in foreign_ingredient_pizzas.items():
        for n_ing, n_pizzas in native_ingredient_pizzas.items():
            if f_pizzas == n_pizzas:
                possible_translations.append((f_ing, n_ing))

    possible_translations.sort()

    for translation in possible_translations:
        print(f"({translation[0]}, {translation[1]})")

    if t < T - 1:
        print()