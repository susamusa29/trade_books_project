from django.contrib import admin
from tradebooks.models import UserProfile
from tradebooks.models import Book
from tradebooks.models import Payment

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('bookName',)}

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book, BookAdmin)
admin.site.register(Payment)
