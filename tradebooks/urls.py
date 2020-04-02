from django.urls import path
from tradebooks import views
"""
note:
# added the index view here
# all good - From Stanislva
changed '' to index instead of login as it makes more sense
added search, about and faq

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
"""
app_name = 'tradebooks'

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # maybe we can use slug for individual products
    path('product/<slug:listing_name_slug>', views.show_listings, name='product'),
    # all books/listing page
    path('books/', views.books, name='books'),

    path('user/', views.user, name='user'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('catalog/', views.catalog, name='catalog'),
    path('search_result/', views.search_result, name='search_result'),
]
