"""django page views.

note:
formatted code, commented unused imports

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
"""

# non-django
# from datetime import datetime
# new one added because of registration form
from tradebooks.forms import UserForm, UserProfileForm

# django

from django.shortcuts import render
# from django.shortcuts import redirect, render
# from django.urls import reverse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse


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


def register(request):
    """Register view."""
    # a value to tell the TEMPLATE whether registration was successful
    registered = False

    # if HTTP POST, then process form data
    if request.method == 'POST':
        # try to grab info from raw form info
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            # save data to database
            user = user_form.save()

            # hash the data
            user.set_password(user.password)
            user.save()

            # delay the saving the model
            profile = profile_form.save(commit=False)
            profile.user = user

            # handle a picture if the user provided it
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # save UserProfile model instance
            profile.save()

            registered = True
        else:
            # in case invalid
            print(user_form.errors, profile_form.errors)
    else:
        # not HTTP POST
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'tradebooks/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def product(request):
    """Product view."""
    return render(request, 'tradebooks/product.html')


def user(request):
    """User view."""
    return render(request, 'tradebooks/user.html')
