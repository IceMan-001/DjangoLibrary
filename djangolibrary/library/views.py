from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


def index(request):
    posts = Book.objects.all()
    context = {
        'title': 'Главная страница сайта',
        'posts': posts
    }
    return render(request, template_name='library/index.html', context=context)


def about(request):
    context = {
        'title': 'О сайте'
    }
    return render(request, template_name='library/about.html', context=context)


def categories(request, cat_id):
    if request.GET:
        print(request.GET)  # <QueryDict: {'name': ['Gagarina'], 'cat': ['music']}>

    return HttpResponse(f'<h1>Категории</h1><p>{cat_id}</p>')


def archive(request, year):
    if int(year) > 2020:
        # raise Http404()
        return redirect('home', permanent=False)  # переход на главную страницу сайта

    return HttpResponse(f'<h1>Категории</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
