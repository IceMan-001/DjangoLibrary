from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
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


def contact(request):
    context = {
        'title': 'Страница контактов'
    }

    return render(request, template_name='library/contact.html', context=context)


def add_page_book(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostForm()
    return render(request, template_name='library/add_page_book.html',
                  context={'form': form, 'title': 'Добавление новой книги'})


def add_page_author(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()
    return render(request, template_name='library/add_page_author.html',
                  context={'form': form, 'title': 'Добавление нового автора'})
