from django.urls import path
from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('registor/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
