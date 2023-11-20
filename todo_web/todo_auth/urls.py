from django.urls import path
from . import views

app_name = 'todo-auth'

urlpatterns = [
    path('login', views.loginpage, name='login'),
    path('signup', views.signup_page, name='signup'),
    path('logout', views.logoutpage, name='logout'),
]