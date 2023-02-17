'''Определяет схемы URL для пользователей'''

from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Страница входа
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Страница выхода
    re_path(r'^logout/$', views.logout_view, name='logout'),
    # Страница регистрации
    re_path(r'^register/$', views.register, name='register')
]
