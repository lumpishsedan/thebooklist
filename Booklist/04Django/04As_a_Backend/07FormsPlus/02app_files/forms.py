from django import forms

from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    author = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}))
    isbn = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'isbn'
        ]
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
