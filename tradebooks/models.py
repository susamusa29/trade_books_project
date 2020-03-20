from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    NAME_MAX_LENGTH = 30

    #This creates a one to one relatioship for the user, the cascade on delete option deletes reference of that upon deletion

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Attributes of user, user model has name, surname attributes
    studentID = models.CharField(max_length=NAME_MAX_LENGTH, blank=True)
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
