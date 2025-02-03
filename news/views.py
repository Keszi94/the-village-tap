from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Article
from .models import CATEGORY_CHOICES
from .forms import ArticleCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def article_list(request, category=None):
    """
    Display a list of :model:`news.Article` filtered by category if provided.

    **Context**
    ``articles``
        A queryset of :model:`news.Article`,
        filtered by status and optionally category.
    ``category``
        A string representing the category title or
        `None` if no category is specified.

    **Template**
    :template:`news/index.html`
    """
    if category:
        # Filter articles by their status (2, Approved) and match the category
        articles = Article.objects.filter(
            status=2,
            category=category).order_by('-created_on')
        # Get the category name to display in the template
        category_title = dict(CATEGORY_CHOICES).get(
             category, 'Unkwown category')
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
    """
    Display a list of :model:`news.Article` filtered by a specific category.

    **Context**
    ``articles``
        A queryset of :model:`news.Article` filtered by the specified category.

    **Template**
    :template:`news/article_list`
    """
    articles = Article.objects.filter(
         category=category).order_by('-created_on')
    return render(request, 'news/article_list', {
        'articles': articles,  # Pass the filtered articles to the template
    })


def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser, login_url='/accounts/login/')
def create_article(request):
    """
    Allow superusers to create a new :model:`news.Article`.

    **Permissions**
    Accessible only to superusers. Unauthorized users are
    redirected to the login page.

    **Context**
    ``form``
        An instance of :form:`news.ArticleCreationForm`.

    **Template**
    :template:`news/create_article.html`
    """
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            # Auto-generating the slug
            article.slug = article.title.lower().replace(' ', '-')
            # Assign current superuser as the author
            article.author = request.user
            # Set the article status to published
            article.status = Article.PUBLISHED
            article.save()
            messages.success(request, 'Your article has been'
                                      'posted successfully!')
            # Redirects to home after submission
            return redirect('home')
    else:
        form = ArticleCreationForm()

    return render(request, 'news/create_article.html', {'form': form})
