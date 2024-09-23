from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127/0/0/1:8000/
    path('about/', about, name='about'),  # http://127/0/0/1:8000/about
    path('page/add_book/', add_page_book, name='add_page_book'),  # http://127/0/0/1:8000/about
    path('page/add_author/', add_page_author, name='add_page_author'),  # http://127/0/0/1:8000/about
    path('page/contact/', contact, name='contact'),  # http://127/0/0/1:8000/about
    path('page/selection/', selection_page, name='selection_page'),  # http://127/0/0/1:8000/about
]
