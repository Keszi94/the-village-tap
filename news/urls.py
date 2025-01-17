from . import views
from django.urls import path, include


urlpatterns = [
    path('create/', views.create_article, name='create_article'),
    path('', views.article_list, name='home'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/<str:category>', views.article_list, name='articles_by_category'),
    path('forum/', include('forum.urls')),
]