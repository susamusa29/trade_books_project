from django.urls import path
from tradebooks import views

app_name = 'tradebooks'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    # maybe we can use slug for individual products
    path('product/', views.product, name='product'),
    path('user/', views.user, name='user')
]
