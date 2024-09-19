from django import forms
from .models import *


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['author', 'name', 'genre', 'year_of_creation']
        model1 = Author
        fields1 = ['first_name', 'patronymic', 'patronymic', 'date_of_birth']

