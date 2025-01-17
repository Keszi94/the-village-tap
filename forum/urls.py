from django.urls import path
from . import views


urlpatterns = [
    path('', views.threads_page, name='threads_page'),
]