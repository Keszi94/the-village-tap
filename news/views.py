from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article
from .models import CATEGORY_CHOICES
from .forms import ArticleCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def article_list(request, category=None):
    if category:
        # Filter articles by their status (2, Approved) and match the category
        articles = Article.objects.filter(status=2, category=category).order_by('-created_on')
        # Get the category name to display in the template
        category_title = dict(CATEGORY_CHOICES).get(category, 'Unkwown category')
    else:
        articles = Article.objects.filter(status=2).order_by('-created_on')
        category_title = None

    return render(request, 'news/index.html', {
    'articles': articles,
    'category': category_title,
    })


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


def articles_by_category(request, category):
    articles = Article.objects.filter(category=category).order_by('-created_on')
    return render(request, 'news/article_list', {
        'articles': articles, # Pass the filtered articles to the template
    })    


# Decorator: restricts the acces to superusers only
@user_passes_test(lambda u: u.is_superuser)
def create_article(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        # Auto-generating the slug
        article.slug = article.title.lower().replace(' ', '-')
        # Assign current superuser as the author
        article.author = request.user
        article.save()
        # Redirects to home after submission
        return redirect('home')
    else:
        form = ArticleCreationForm()

    return render(request, 'news/create_article.html', {'form': form})        


