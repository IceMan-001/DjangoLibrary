from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .forms import AddPostForm
from .models import *


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    print(books, authors)
    context = {
        'title': 'Главная страница сайта',
        'books': books,
        'authors': authors
    }
    return render(request, template_name='library/index.html', context=context)


def about(request):
    context = {
        'title': 'О сайте'
    }
    return render(request, template_name='library/about.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def addpage(request):
    form = AddPostForm()
    context = {
        'form': form,
        'title': 'Добавление новой записи'
    }
    return render(request, template_name='library/addpage.html', context=context)


def contact(request):
    context = {
        'title': 'Страница контактов'
    }

    return render(request, template_name='library/contact.html', context=context)
