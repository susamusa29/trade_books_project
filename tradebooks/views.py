"""django page views.

note:
formatted code, commented unused imports
added search, faq and about
added paginator to listing

todo:
add paginator to listings, catalog and user.

author: Teoh Yee Hou (2471020t)
        Stanislava Dyakova (2390717d)
        Abrar Haroon (2513933h)
"""

import smtplib

from email.message import EmailMessage


from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

# non-django
# new one added because of registration form
from tradebooks.forms import UserForm, UserProfileForm, BookForm, UserEditForm
from tradebooks.forms import ListingForm, ContactForm
from tradebooks.models import Listing, Book
from . import config
from . import forms


# django


def index(request):
    """Index view.

    todo:
        add context dicts
        cookie handler
    """

    return render(request, 'tradebooks/index.html', context={
        "carouselItems": Listing.objects.all().order_by("-id")[:3],
        "latestListings": Listing.objects.all().order_by("-id")[3:12],
    })


# only people who have logged in can access this view
@login_required
# view for logging out sign out button
def user_logout(request):
    # use of logout method to log out the user
    logout(request)
    # goes back to home
    return redirect(reverse('tradebooks:index'))


def user_login(request):
    # pull relevent info if pos request
    if request.method == 'POST':
        # username and password needed
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if combination is valid
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                # if the accunt is valid and active we can log the user in
                login(request, user)
                return redirect(reverse('tradebooks:index'))
            else:
                return HttpResponse("The account you entered is disabled.")
        else:
            # wrong details
            print(f"Invalid login details: {username}, {password}")
            return redirect(reverse('tradebooks:login'))
    else:
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

        if (user_form.is_valid() and profile_form.is_valid()):
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


# view to show listed products
# maybe we need a view to list products?
# def list_product(request):

def product(request):
    """Product view."""

    return render(request, 'tradebooks/product.html')


# adding a book functionality view
@login_required
def add_book(request):
    # value to tell the template whether addition is successful
    added = False
    user = request.user.id

    if (request.method == 'POST'):
        # creating a form object
        # taking information from the form information
        book_form = BookForm(request.POST)
        listing_form = ListingForm(request.POST)

        if (book_form.is_valid() and listing_form.is_valid()):
            # book.bookSold = user
            # save form to database
            book = book_form.save(commit=False)

            if 'bookImage' in request.FILES:
                book.bookImage = request.FILES['bookImage']

            book.save()
            listing = listing_form.save(commit=False)
            listing.book = book
            listing.user = request.user.userprofile
            listing.save()

            added = True
            messages.success(request, "Your listing has been added.")
        else:
            messages.error(request, "Your listing was not added.")
            print(book_form.errors, listing_form.errors)
    else:
        book_form = BookForm()
        listing_form = ListingForm()

    return render(request,
                  'tradebooks/add_book.html',
                  context={'book_form': book_form,
                           "listing_form": listing_form,
                           'added': added})

    # view to add books
    return render(request, 'tradebooks/add_book.html')


def show_listing(request, listing_name_slug):
    """Show individual product listing"""
    contextDict = {}
    try:

        listing = Listing.objects.get(slug=listing_name_slug)
        contextDict["listing"] = listing



    except Listing.DoesNotExist:
        contextDict["listing"] = None
        contextDict["book"] = None

    return render(request, 'tradebooks/product.html', context=contextDict)


#
def books(request):
    """Show all product listings"""
    all_listings = Listing.objects.all().order_by("id")

    # test limit to 3 listings as there ara only 4 listings in populate.
    # will add more.
    paginator = Paginator(all_listings, 6)

    page = request.GET.get('page')

    listing = paginator.get_page(page)

    return render(request, 'tradebooks/books.html', context={
        "listings": listing,
    })


def delete_listing(request, listing_name_slug):
    listing = get_object_or_404(Listing, slug=listing_name_slug)

    lister = listing.user.user

    if request.method == "POST" and \
            request.user.is_authenticated and \
            request.user == lister:

        if request.POST.get('deleteBook', 'dne') == '':
            delete_book = Book.objects.get(id=listing.book.id)
            delete_book.delete()
            messages.success(request, "Book successfully deleted!")

        listing.delete()
        messages.success(request, "Listing successfully removed!")
        return redirect(reverse('tradebooks:user'))

    context = {'listing': listing,
               'lister': lister,
               }

    return render(request, 'tradebooks/delete_listing.html', context)


@login_required
def user(request):
    """User view."""

    # context_dict = {}
    #
    # showlisting(context_dict, listing_name_slug)
    all_listing = Listing.objects.filter(user=request.user.userprofile)
    paginator = Paginator(all_listing, 12)

    page = request.GET.get('page')

    listings = paginator.get_page(page)

    return render(request, 'tradebooks/user.html', context={
        "listings": listings,
    })


# code to edit a profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('tradebooks:user'))
    else:
        form = UserEditForm(instance=request.user)
        args = {'form': form}

    return render(request, 'tradebooks/edit_profile.html', args)


@login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect(reverse('tradebooks:user'))
#         else:
#             return redirect('tradebooks:about')
#     else:
#         form = PasswordChangeForm(user=request.user)
#         args = {'form':form}
#
#     return render(request, 'tradebooks/change_password.html', args)
def change_password(request):
    """Change password view.
    Note:
    (teoh) previous version does not work so it is replaced by this version.
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user_form = form.save()
            update_session_auth_hash(request, user_form)
            messages.success(request, 'Your password has been changed!')
            return redirect(reverse('tradebooks:user'))


    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'tradebooks/change_password.html', context={
        'form': form
    })


def catalog(request):
    """Catalog view."""
    all_books = Book.objects.order_by("bookName")
    paginator = Paginator(all_books, 6)

    page = request.GET.get('page')

    books = paginator.get_page(page)

    return render(request, 'tradebooks/catalog.html', context={
        "books": books
    })


def help(request):
    return render(request, 'tradebooks/help.html')


def contactus(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted." +
                             " We will contact you shortly.")

    else:
        form = ContactForm()
    return render(request, 'tradebooks/contactus.html', {'form': form})


def search(request):
    """Search view."""
    return render(request, 'tradebooks/search.html')


def about(request):
    """About view."""
    return render(request, 'tradebooks/about.html')


def faq(request):
    """FAQ view."""
    return render(request, 'tradebooks/faq.html')


# def search_result(request):
#     if request.method == "GET":
#         query = request.GET.get("search")
#
#         submit_button = request.GET.get("submit")
#
#         if query is not None:
#             lookups = Q(title__icontains=query)|
#                       Q(content__icontains=query)
#
#             results = Post.objects.filter(lookups).distinct()
#
#             context={'results': results,
#                      'submitbutton': submit_button}
#
#             return render(request, 'tradebooks/search_result.html', context)
#         else:
#             return render(request, 'tradebooks/search_result.html')
#     else:
#         return render(request, 'tradebooks/search_result.html')

def search_result(request):
    """Search results view.

    splits the query then iterates through it, filtering disting results"""
    if request.method == 'GET':
        query = request.GET.get('search')

        submit_button = request.GET.get('submit')

        if query:
            # old lookup
            # lookups = Q(bookName__icontains=query) | Q(bookISBN__icontains=query) | Q(bookAuthor__icontains=query) | \
            #           Q(course__icontains=query)
            #
            # books = Book.objects.filter(lookups).distinct()
            books = Book.objects.all()

            # splits the query for individual words.
            words = query.split()
            # lookup_dict = {"book_name": bookName__icontains,
            #                ""}
            # lookups = ["bookName__icontains",
            #            "bookISBN__icontains",
            #            "course__icontains",
            #            ]
            # searchlist = ["eval({})={}".format(l, w) for l in lookups for w in words ]
            # search = [Q(eval(s))for s in searchlist]
            # search = [Q((eval(l)="{}".format(l,w))) for l in lookups for w in words]
            # lookup = search[0]
            # for i in range(len(search)):
            #     if i != 0:
            #         lookup = lookup | search[i]

            # for w in words:
            #     for l in lookups:

            # iterates through words list.
            for w in words:
                lookup = Q(bookName__icontains=w) | \
                         Q(bookISBN__icontains=w) | \
                         Q(course__icontains=w) | \
                         Q(bookAuthor__icontains=w)
                books = books.filter(lookup).distinct()

            # lookup = reduce(lambda x, y: x | y, search)
            # books = Book.objects.filter(lookup).distinct()

            context_dict = {'books': books,
                            'submit_button': submit_button,
                            'listings': Listing.objects.all()}

            return render(request, 'tradebooks/search_result.html', context_dict)

        else:
            return render(request, 'tradebooks/search_result.html')

    else:
        return render(request, 'tradebooks/search_result.html')


# added(API)
def button(request):
    return render(request, 'home.html')


# external function obtains email from the user and sends them a confirmation in real time
# # configuration settings for sensitive data in email in config.py
# # home.html contains the form and button functionalitys

def external(request):
    form = forms.HomeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            to_email = form.cleaned_data.get('post')
            post = form.save(commit=False)
            post.is_active = False
            mail_subject = config.EMAIL_SUBJECT
            message = config.EMAIL_MESSAGE
            EMAIL_ADDRESS = config.EMAIL_HOST_USER
            EMAIL_PASSWORD = config.EMAIL_HOST_PASSWORD

            msg = EmailMessage()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = to_email
            msg['subject'] = mail_subject
            msg.set_content(message)
            with smtplib.SMTP_SSL(config.EMAIL_HOST, config.EMAIL_PORT) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
                messages.success(request, 'Thank you')
            return HttpResponseRedirect('/tradebooks/books/')

    else:

        return render(request, 'home.html', {'form': form})

# def book_list(request, category_slug=None):
#     category=None
#     categories = Category.objects.all()
#     books = Books.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category, category_slug=category_slug)
#         books = books.filter(category=category)
