from django.shortcuts import render


def index(request):
    foods = ['apple', 'banana', 'coconut', ]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }
    return render(request, 'index.html', context)
