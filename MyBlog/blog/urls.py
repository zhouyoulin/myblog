from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path("blog_title", views.blog_title, name='blog_title'),
    path(r'content/<article_id>', views.blog_details, name='blog_details'),
]