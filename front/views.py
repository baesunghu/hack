from django.http import HttpResponse
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
    return render(request, 'front/index.html', context)
