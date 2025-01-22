from .models import Article
from django import forms
from django_summernote.widgets import SummernoteWidget

# not using crispy because I prefer not to
class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['slug', 'created_on', 'status', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # using 'rows': to control the height of the text areas
            'blurb': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'content': SummernoteWidget(attrs={'class': 'form-control', 'rows': 5}),
            'sources': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Textarea(attrs={'class': 'form-control'}),
        }

    # Get the logged in superuser's name for the author
    def __init__(self, *args, **kwargs):
        user = kwargs.get('user', None)
        super(ArticleCreationForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['author'].initial = user


