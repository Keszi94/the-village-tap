from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article

# Create your views here.

class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=2)
    template_name = "news/index.html"
    paginate_by = 6


def article_detail(request, slug):
    """
    Display an individual :model:`news.Article`.

    **Context**

    ``article``
        An instance of :model:`news.Article`.

    **Template:**

    :template:`news/article_detail.html`
    """

    queryset = Article.objects.filter(status=2)
    article = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "news/article_detail.html",
        {"article": article},
    )    

