from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','author','genre','release_date','rating','cover']
        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'}),
        }
