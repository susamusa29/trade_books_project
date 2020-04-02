from django.contrib import admin
from tradebooks.models import UserProfile
from tradebooks.models import Book, Category
from tradebooks.models import Payment
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class BookAdmin(admin.ModelAdmin):
    # list_filter = ['category']
    prepopulated_fields = {'slug':('bookName',)}

# Register your models here.

admin.site.register(UserProfile)
# admin.site.register(Book, BookAdmin, CategoryAdmin)
admin.site.register(Book, BookAdmin, CategoryAdmin)
admin.site.register(Payment)
