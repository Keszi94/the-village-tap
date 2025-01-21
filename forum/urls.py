from django.urls import path
from . import views


urlpatterns = [
    # Delete thread
    path('<slug:slug>/delete/', views.delete_thread, name='delete_thread'),
    # Edit thread
    path('<slug:slug>/edit', views.edit_thread, name='edit_thread'),
    # Individual threads
    path('<slug:slug>/', views.thread_detail, name='thread_detail'),
     # Threads page
    path('', views.threads_page, name='threads_page'),
]