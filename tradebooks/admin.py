from django.contrib import admin
from tradebooks.models import UserProfile
from tradebooks.models import Book
from tradebooks.models import Payment

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Payment)
