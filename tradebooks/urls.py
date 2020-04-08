from django.urls import path
from tradebooks import views
from django.contrib import admin
"""
note:
# added the index view here
# all good - From Stanislva
changed '' to index instead of login as it makes more sense
added search, about and faq

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
        Abrar Haroon
"""
app_name = 'tradebooks'

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # maybe we can use slug for individual products
    path('product/<slug:listing_name_slug>/', views.show_listing, name='product'),
    # all books/listing page
    path('books/', views.books, name='books'),
    path('user/', views.user, name='user'),
     # will add a book url
    path('add/', views.add_book, name='add'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('catalog/', views.catalog, name='catalog'),
    path('search_result/', views.search_result, name='search_result'),
    path('contactus/', views.contactus, name='contactus'),
    path('help/', views.help, name='help'),
    path('email/', views.button, name='api'),
    path('external/', views.external, name='external'),
    path('user/edit/', views.edit_profile, name='edit_profile'),
    path('edit/', views.edit_profile, name='edit'),
    path('user/password/', views.change_password, name="change-password"),
    path('product/<slug:listing_name_slug>/delete_listing/', views.delete_listing, name="delete_listing"),
]
