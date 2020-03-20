from django.db import models
from django.contrib.auth.models import User

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



    def __str__(self):
        return self.user.username


# The second model will be the book model

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

# Some foreign keys for the 1:N relationships
# on_delete

    bookSold = models.ForeignKey(UserProfile, related_name = 'book_sellers',on_delete = models.CASCADE)
    bookBought = models.ForeignKey(UserProfile, related_name = 'book_buyers',on_delete = models.CASCADE)

# Have to add payments when models is created 
