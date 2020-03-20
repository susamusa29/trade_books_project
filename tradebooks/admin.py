from django.contrib import admin
from tradebooks.models import UserProfile
from tradebooks.models import Book

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)