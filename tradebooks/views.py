"""django page views.

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
"""

# non-django
from datetime import datetime

# django

from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    """Index view.

    todo:
        add context dicts
        cookie handler
    """
    return render(request, 'tradebooks/index.html')


def user_login(request):
    """User login view."""
    return render(request, 'tradebooks/login.html')


def product(request):
    """Product view."""
    return render(request, 'tradebooks/product.html')


def user(request):
    """User view."""
    return render(request, 'tradebooks/user.html')
