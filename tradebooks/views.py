"""django page views.

note:
formatted code, commented unused imports
added search, faq and about

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
"""

# non-django
from datetime import datetime
    #new one added because of registration form
from tradebooks.forms import UserForm, UserProfileForm, BookForm
from tradebooks.models import UserProfile
from tradebooks.models import Listing
# django

from django.shortcuts import render
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

#only people who have logged in can access this view 
@login_required
#view for logging out sign out button
def user_logout(request):
    #use of logout method to log out the user
    logout(request)
    #goes back to home
    return redirect(reverse('tradebooks:index'))

def user_login(request):
    #pull relevent info if pos request
    if request.method == 'POST':
        #username and password needed
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if combination is valid
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                # if the accunt is valid and active we can log the user in
                login(request, user)
                return redirect(reverse('tradebooks:index'))
            else:
                return HttpResponse("The account you entered is disabled.")
        else:
            #wrong details
            print(f"Invalid login details: {username}, {password}")
            return render (request, 'index.html')
    else:
        return render(request,'tradebooks/login.html')


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
    
    return render(request, 'tradebooks/register.html', context = {'user_form': user_form, 'profile_form': profile_form,'registered': registered})
        
#view to show listed products
#maybe we need a view to list products?
# def list_product(request):

def product(request):
    """Product view."""

    return render(request, 'tradebooks/product.html')

#adding a book functionality view
@login_required
def add_book(request):
    form = BookForm()
    #view to add books#
    return render(request, 'tradebooks/add_boook.html', {'form':form})

def show_listings(request, listing_name_slug):
    """Show all books/listing view."""
    contextDict = {}
    try:
        listing = Listing.objects.get(slug=listing_name_slug)
        contextDict["listing"] = listing

    except Listing.DoesNotExist:
        contextDict["listing"] = None

    return render(request, 'tradebooks/books.html', context=contextDict)

#
def books(request):
    return render(request, 'tradebooks/books.html', context={
        "listings": Listing.objects.all(),
    })



def user(request):
    """User view."""

    # context_dict = {}
    #
    # showlisting(context_dict, listing_name_slug)



    return render(request, 'tradebooks/user.html')




def search(request):
    """Search view."""
    return render(request, 'tradebooks/search.html')


def about(request):
    """About view."""
    return render(request, 'tradebooks/about.html')


def faq(request):
    """FAQ view."""
    return render(request, 'tradebooks/faq.html')

# def book_list(request, category_slug=None):
#     category=None
#     categories = Category.objects.all()
#     books = Books.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category, category_slug=category_slug)
#         books = books.filter(category=category)