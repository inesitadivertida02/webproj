# myapp/forms.py
from django import forms

from app.models import Book


# Create your forms here.
class BookQueryForm(forms.Form):
    query =forms.CharField(label='Search:', max_length=100)
class BookSearchForm(forms.Form):
    title = forms.CharField(required=False, max_length=100, label='Title')
    author = forms.CharField(required=False, max_length=100, label='Author')
    publisher = forms.CharField(required=False, max_length=100, label='Publisher')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'date', 'authors', 'publisher']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'authors': forms.CheckboxSelectMultiple(),
        }

