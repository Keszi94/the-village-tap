from django import forms
from .models import Article


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['slug', 'created_on', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # using 'rows': to control the height of the text areas
            'blurb': forms.TextInput(attrs={'class': 'form-control', 'rows': 2}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'sources': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Textarea(attrs={'class': 'form-control'}),
        }