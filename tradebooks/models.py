from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.

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
    bookID = models.IntegerField(primary_key = True)

# Remark :
# maybe suitable for database to add all courses for the search API

# Additional attributes
    bookName = models.CharField(max_length = BOOK_NAME_MAX_LEBGTH)
    bookImage = models.ImageField(upload_to='profile_images', blank=True)
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

# Some foreign keys for the 1:N relationships
# on_delete

    bookSold = models.ForeignKey(UserProfile, related_name = 'book_sellers',on_delete = models.CASCADE, null= True, blank=True)
    bookBought = models.ForeignKey(UserProfile, related_name = 'book_buyers',on_delete = models.CASCADE, null=True, blank=True)

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



