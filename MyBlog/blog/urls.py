from django.urls import path
from . import views

urlpatterns = [
    path("blog_title", views.blog_title),
    path("<article_id>", views.blog_details, name='blog_details'),
]