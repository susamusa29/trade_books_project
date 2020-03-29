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
