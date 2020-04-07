"""Model registration on admin site.

Note:
added listing, condensed imports to a single line (Teoh)
added contact us (teoh)

author: Stanislava Dyakova (2390717d)
        Teoh Yee Hou (2471020t)
"""

from django.contrib import admin
from tradebooks.models import UserProfile, Book, Payment, Listing, ContactUs

# commented out some stuff for code to work for now.
# from tradebooks.models import Category
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

class BookAdmin(admin.ModelAdmin):
    # list_filter = ['category']
    prepopulated_fields = {'slug':('bookName',)}

# Register your models here.

admin.site.register(UserProfile)
# admin.site.register(Book, BookAdmin, CategoryAdmin)
admin.site.register(Book, BookAdmin)
# commented out this for code to work for now(teoh)
# admin.site.register(Book, BookAdmin, CategoryAdmin)
admin.site.register(Payment)
admin.site.register(Listing)
admin.site.register(ContactUs)
