import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    response = ''
    for item in os.listdir('.'):
        if os.path.isdir(os.path.join('.', item)):
            response += f"- {item}\n"

    for item in os.listdir('.'):
        if os.path.isfile(os.path.join('.', item)):
            response += f"{item}\n"
    return HttpResponse(response, content_type="text/plain")

