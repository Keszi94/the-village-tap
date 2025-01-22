from django import forms
from .models import Thread, Comment


class ThreadCreationForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'description', 'related_article_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter thread title' }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your thread description'}),
            'related_article_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Paste related article URL (Optional)'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }
