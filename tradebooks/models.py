"""Models.

Note:
added custom save for users(teoh) and books(Stanislava)
added listing
edited to remove bookID, foreign key for listing to point to book so its a more
polished approach overall.
changed slug to include book id, book name and username to allow duplicate
listings but different id
added contact us model

todo:
remove price from listing as book already have it.

author: Stanislava Dyakova (2390717d)
        Teoh Yee Hou (2471020t)
"""


from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
#Category models for categories and searches

# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique = True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

    # def get_absolute_url(self):
    #     return reverse()

#The first model is the user model

class UserProfile(models.Model):

    NAME_MAX_LENGTH = 30

    #This creates a one to one relatioship for the user, the cascade on delete option deletes reference of that upon deletion

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Attributes of user, user model has name, surname attributes
    studentID = models.CharField(max_length=NAME_MAX_LENGTH, blank=True, primary_key = True)
    #add pic attribute upon creating a media directory

    #the main course of student
    courseMain = models.CharField(max_length=NAME_MAX_LENGTH, blank=True)

    #year the student is in
    year = models.IntegerField(default=1)

    #user's picture
    picture = models.ImageField(upload_to='profile_images', blank=True)

    #user prfile validation (will be inserted at a later point)

    #the date of a profile is an attribute that already exists in the user interface

    # teoh: custom save:
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)


    def __str__(self):
        return self.user.username   # The second model will be the book model
# Think of toString method for book, return will be the name but still authr will be needed
# therefore, both should be included ?
class Book(models.Model):
    BOOK_CODE_MAX_LENGTH = 120
    BOOK_NAME_MAX_LEBGTH = 100
    AUTHOR_NAME_MAX_LENGTH = 50
    COURSE_NAME_MAX_LENGTH = 30
    BOOK_DESCRIPTION_MAX_LENGTH = 200

    bookISBN = models.CharField(max_length = BOOK_CODE_MAX_LENGTH, blank = True)

#   we will be autogenerating a primary key
#   (However, Django offers the same automatic ID, so probably unnecesary)
#     bookID = models.IntegerField(primary_key = True)

# Remark :
# maybe suitable for database to add all courses for the search API

# Additional attributes
    bookName = models.CharField(max_length = BOOK_NAME_MAX_LEBGTH)
    bookImage = models.ImageField(upload_to='book_images', blank=True)
    bookAuthor = models.CharField(max_length=AUTHOR_NAME_MAX_LENGTH)
    course = models.CharField(max_length=COURSE_NAME_MAX_LENGTH)
    year=models.IntegerField(default=1)
    bookDescription=models.CharField(max_length=BOOK_NAME_MAX_LEBGTH)
    price = models.DecimalField(decimal_places=2, max_digits = 4, default=0)
    currency = models.CharField(
        max_length=3,
        default='GBP',
        blank=True
    )
    slug = models.SlugField(unique=True, default='')
    # category = models.ForeignKey(Category, related_name='books')

# Some foreign keys for the 1:N relationships
# on_delete

    bookSold = models.ForeignKey(UserProfile, related_name = 'book_sellers',on_delete = models.CASCADE, null= True, blank=True)
    bookBought = models.ForeignKey(UserProfile, related_name = 'book_buyers',on_delete = models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.bookName)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.bookName

# Have to add payments when models is created 
# I think it is better to have a one to one relationship with payment and book in payment because it is safer. It is not safe to transfer
# payment relationships in another table, in my opinion

    # payID = models.ForeignKey(Payment, on_delete = models.CASCADE, default = None)

# Foreign Key user due to one to many relationship with payment

class Payment(models.Model):
    paymentID = models.IntegerField(primary_key = True, default=0)
    processed = models.BooleanField(default = False)

    #Foreign Keys
    payee = models.ForeignKey(UserProfile, related_name ='payment_payee', on_delete = models.CASCADE)

    #OnetoOne reltionship with the bough book( One payment can be maid per book)
    book_bought = models.OneToOneField(Book, related_name = 'book_bought', on_delete = models.CASCADE, default = None)


# teoh's addition
class Listing(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    info = models.CharField(max_length=3000, default="", blank=True)
    # price = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # book = models.CharField(max_length=128)

    slug = models.SlugField(unique=True, default="")

    def save(self, *args, **kwargs):
        self.slug = slugify("{} {} {}".format(self.book.id,
                                              self.book,
                                              self.user))
        super(Listing, self).save(*args, **kwargs)

    def __str__(self):
        return self.book.bookName

class ContactUs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.title

#API Use
class Post(models.Model):
    post = models.CharField(max_length=128, unique=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

# class Category(models.Model):
#     """Category model.
#     (added by teoh)
#     """
#     NAME_MAX_LENGTH = 30
#
#     name = models.CharField(max_length = NAME_MAX_LENGTH, unique=True)
#     slug = models.SlugField(unique=True, default="")
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)
#
#     class Meta:
#         """Plural spelling."""
#         verbose_name_plural = "Categories"
#
#     def __str__(self):
#         return self.name
