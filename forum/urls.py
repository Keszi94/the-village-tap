from django.urls import path
from . import views


urlpatterns = [
    path('', views.threads_page, name='threads_page'),
    path('forum/<slug:slug>/', views.thread_detail, name='thread_detail'),
]