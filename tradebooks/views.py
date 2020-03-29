<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    return render(request, 'tradebooks/login.html')
=======
# non-django
from datetime import datetime

# django

from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def product(request):
    return render(request, 'tradebooks/product.html')


def user(request):
    return render(request, 'tradebooks/user.html')
>>>>>>> origin/Teoh
