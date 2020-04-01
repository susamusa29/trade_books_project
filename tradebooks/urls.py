"""Urls for tradebooks.

note:
# added the index view here
# all good - From Stanislva
changed '' to index instead of login as it makes more sense
added faq , about and search page.

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
"""

from django.urls import path
from tradebooks import views


app_name = 'tradebooks'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('index/', views.index, name='index'),
=======
    # path('index/', views.index, name='index'),
>>>>>>> 994808b0e6bd35c488fa4cad311d147049698d0c
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # maybe we can use slug for individual products
    path('product/', views.product, name='product'),
    path('user/', views.user, name='user'),
    path('register/', views.register, name='register'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search')
]
