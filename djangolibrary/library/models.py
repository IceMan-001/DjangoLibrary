from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=150, verbose_name='Фамилия автора книги')
    name = models.CharField(max_length=150, verbose_name='Название')
    genre = models.CharField(max_length=150, verbose_name='Жанр')
    year_of_creation = models.CharField(max_length=10, verbose_name='Год написания')
    author_name = models.ForeignKey(
        'Author', on_delete=models.CASCADE, max_length=150, verbose_name='Автор')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'


class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, blank=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    date_of_birth = models.CharField(max_length=255, verbose_name='Дата рождения')

    def __str__(self):
        return self. last_name
