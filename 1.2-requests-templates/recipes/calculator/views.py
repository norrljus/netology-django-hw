from django.shortcuts import render


DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
    "burger": {
        "мясные котлеты гриль, шт.": 2,
        "специальный соус, гр": 10,
        "сыр, ломтики шт.": 2,
        "огурцы, нарезанные колясики шт.": 6,
        "салат, листочки шт.": 2,
        "лук, кружки лука шт.": 2,
        "булочка с кунжутом, шт.": 2,
    },
}


def index(request, recipe_name):
    if recipe_name in DATA:
        data = DATA[recipe_name]
        servings = int(request.GET.get("servings", 1))
        if servings > 1:
            result = dict()
            for ingredient, value in data.items():
                all_ingredients = round(value * servings, 1)
                result[ingredient] = all_ingredients
            context = {
                "recipe_name": recipe_name,
                "recipe": result,
                "servings": f"{servings} peoples",
            }
        else:
            context = {"recipe_name": recipe_name, "recipe": data, "servings": "one"}
    else:
        context = None
    return render(request, "calculator/index.html", context)
