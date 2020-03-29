from django.urls import path
<<<<<<< HEAD
from rango import views
=======
from tradebooks import views
>>>>>>> origin/Teoh

app_name = 'tradebooks'

urlpatterns = [
<<<<<<< HEAD
    path('', views.user_login, name = 'login'),
    path('login/', views.user_login, name='login'),
]
=======
    # maybe we can use slug for individual products
    path('product/', views.product, name='product'),
    path('user/', views.user, name='user')
]
>>>>>>> origin/Teoh
