# from customer.models import Book
from django import forms
from customer.models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'category', 'price', 'file', 'description', 'publisher', 'published']