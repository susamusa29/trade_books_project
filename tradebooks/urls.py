from django.urls import path
from rango import views

app_name = 'tradebooks'

urlpatterns = [
    path('', views.user_login, name = 'login'),
    path('login/', views.user_login, name='login'),
]