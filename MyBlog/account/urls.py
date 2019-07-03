from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("register/", views.user_register, name="user_register"),
    path("userInfo/<user_id>", views.user_info, name="user_info"),
]