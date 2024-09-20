from django import forms
from .models import *


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author_name'].empty_label = 'Автор не выбран'

    class Meta:
        model = Book
        fields = ['author_name', 'name', 'genre', 'year_of_creation', 'author']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'patronymic', 'last_name', 'date_of_birth']
