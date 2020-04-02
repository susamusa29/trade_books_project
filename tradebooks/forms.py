from django import forms
from django.contrib.auth.models import User
from tradebooks.models import UserProfile, Book,Post
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('studentID','courseMain','year','picture', )

#form for books, will be the same as sign up but for books
class BookForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Book
        fields = ('bookName', 'bookImage', 'bookAuthor', 'course', 'year', 'bookDescription', 'price', 'currency', 'slug', 'bookISBN')
        exclude = ('bookSold', 'bookBought')
        
# API
# provides functionality for the form used in home.html
class HomeForm(forms.ModelForm):

    post = forms.CharField

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Post
        fields = ('post',)

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
