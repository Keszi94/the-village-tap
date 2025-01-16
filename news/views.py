from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.

class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=2)
    template_name = "news/index.html"
    paginate_by = 6

