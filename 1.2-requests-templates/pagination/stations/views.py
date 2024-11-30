import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV

stations = []
with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stations.append(row)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    paginator = Paginator(stations, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
         'bus_stations': paginator.get_page(current_page),
         'page': page,
    }
    return render(request, 'stations/index.html', context)
