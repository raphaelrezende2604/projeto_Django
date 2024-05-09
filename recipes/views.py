from django.shortcuts import render
from django.http import HttpResponse


def home(resquest):
    return render(resquest, 'recipes/pages/home.html')

