from django.urls import path
from tradebooks import views
"""
note:
# added the index view here
# all good - From Stanislva
changed '' to index instead of login as it makes more sense

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
"""
app_name = 'tradebooks'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    # maybe we can use slug for individual products
    path('product/', views.product, name='product'),
    path('user/', views.user, name='user'),
    path('register/', views.register, name='register'),
]
