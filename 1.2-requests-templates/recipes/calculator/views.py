from django.shortcuts import render


DATA = {
    'omlet': {
        'eggs, whole': 2,
        'milk, l.': 0.1,
        'salt, tsp.': 0.5,
    },
    'pasta': {
        'pasta, g.': 0.3,
        'cheese, g.': 0.05,
    },
    'sandwich': {
        'bread, slice': 1,
        'ham, slice': 1,
        'cheese, slice': 1,
        'tomato, slice': 1,
    },
    'milkshake': {
        'milk, l.': 0.5,
        'ice cream, g.': 100,
        'sauce, tbsp.': 1,
    },
}


def recipe(request, rec):
    serv = int(request.GET.get("servings", 1))
    context = {
        'name': rec,
        'recipe': DATA[rec],
        'servings': serv,
    }
    return render(request, "calculator/index.html", context)
