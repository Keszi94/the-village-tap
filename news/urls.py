from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', views.create_article, name='create_article'),
    path('', views.article_list, name='home'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/<str:category>',
         views.article_list, name='articles_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(
         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
