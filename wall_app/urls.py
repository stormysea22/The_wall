from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall_index),
    path('posts/create', views.create_post),
    path('comments/create', views.create_comment),
    path('comments/<int:comment_id>/delete', views.delete_comment),
    path('posts/<int:post_id>/delete', views.delete_post)
]