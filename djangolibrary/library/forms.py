from django import forms
from .models import *


class AddPostForm(forms.Form):
    author = models.CharField(max_length=150, verbose_name='Автор')
    name = models.CharField(max_length=150, verbose_name='Название')
    genre = models.CharField(max_length=150, verbose_name='Жанр')
    year_of_creation = models.DateField(verbose_name='Год написания')
    author_name = models.ForeignKey('Author', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
