from django.urls import path
from . import views


urlpatterns = [
    # Thread CRUD paths:
    # 1. Delete thread
    path('<slug:slug>/delete/', views.delete_thread, name='delete_thread'),
    # 2. Edit thread
    path('<slug:slug>/edit', views.edit_thread, name='edit_thread'),

    # Comment CRUD paths:
    # 1. Edit comment
    path('<slug:slug>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    # 2 Delete comment
    path('delete_comment/<slug:slug>/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),

    # Individual threads
    path('<slug:slug>/', views.thread_detail, name='thread_detail'),
    # Threads page
    path('', views.threads_page, name='threads_page'),
]
