
# run $ python manage.py test tests_4,7
# 
# The tests will then be run, and the output displayed -- do you pass them all?
# 
# Once you are done with the tests, delete the module. You don't need to put it in your Git repository!
#

import os
import inspect
from tradebooks.models import Book, UserProfile
from populate_tradebooks import populate
from django.test import TestCase
from django.urls import reverse, resolve
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}Tradebooks TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class FormClassTests(TestCase):
    """
    Do the Form classes exist, and do they contain the correct instance variables?
    """
    def test_module_exists(self):
        """
        Tests that the forms.py module exists in the expected location.
        """
        project_path = os.getcwd()
        tradebooks_app_path = os.path.join(project_path, 'tradebooks')
        forms_module_path = os.path.join(tradebooks_app_path, 'forms.py')

        self.assertTrue(os.path.exists(forms_module_path), f"{FAILURE_HEADER}We couldn't find tradebooks's new forms.py module. This is required to be created at the top of Section 7.2. This module should be storing your two form classes.{FAILURE_FOOTER}")
    
    def test_Book_form_class(self):
        """
        Does the BookForm implementation exist, and does it contain the correct instance variables?
        """
        # Check that we can import BookForm.
        import tradebooks.forms
        self.assertTrue('BookForm' in dir(tradebooks.forms), f"{FAILURE_HEADER}The class BookForm could not be found in tradebooks's forms.py module. Check you have created this class in the correct location, and try again.{FAILURE_FOOTER}")

        from tradebooks.forms import BookForm
        Book_form = BookForm()

        # Do you correctly link Book to BookForm?
        self.assertEqual(type(Book_form.__dict__['instance']), Book, f"{FAILURE_HEADER}The BookForm does not link to the Book model. Have a look in the BookForm's nested Meta class for the model attribute.{FAILURE_FOOTER}")

        # Now check that all the required fields are present, and of the correct form field type.
        fields = Book_form.fields

        expected_fields = {
            'bookName': django_fields.CharField,
            'year': django_fields.IntegerField,
            'course': django_fields.CharField,
            'bookAuthor': django_fields.CharField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your BookForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field '{expected_field_name}' in BookForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")

class BookFormAncillaryTests(TestCase):
    """
    Performs checks to see if all the additional requirements in Chapter 7 for adding a BookForm have been implemented correctly.
    Checks URL mappings and server output.
    """
    def test_add_book_url_mapping(self):
        """
        Tests whether the URL mapping for adding a Book is resolvable.
        """
        try:
            resolved_name = resolve('/tradebooks/add/').view_name
        except:
            resolved_name = ''
        
        self.assertEqual(resolved_name, 'tradebooks:add', f"{FAILURE_HEADER}The lookup of URL '/tradebooks/add/' didn't return a mapping name of 'tradebooks:add'. Check you have the correct URL mapping for adding a Book, and try again.{FAILURE_FOOTER}")
    
    
    
   

class UserProfileFormClassTests(TestCase):
    """
    Checks whether the UserProfileForm class has been implemented correctly.
    """
    def test_userprofile_form_class(self):
        """
        Does the UserProfileForm implementation exist, and does it contain the correct instance variables?
        """
        # Check that we can import UserProfileForm.
        import tradebooks.forms
        self.assertTrue('UserProfileForm' in dir(tradebooks.forms), f"{FAILURE_HEADER}The class UserProfileForm could not be found in tradebooks's forms.py module. Check you have created this class in the correct location, and try again.{FAILURE_FOOTER}")

        from tradebooks.forms import UserProfileForm
        userprofile_form = UserProfileForm()

        # Do you correctly link UserProfile to UserProfileForm?
        self.assertEqual(type(userprofile_form.__dict__['instance']), UserProfile, f"{FAILURE_HEADER}The UserProfileForm does not link to the UserProfile model. Have a look in the UserProfileForm's nested Meta class for the model attribute.{FAILURE_FOOTER}")

        # Now check that all the required fields are present, and of the correct form field type.
        fields = userprofile_form.fields

        expected_fields = {
            'studentID': django_fields.CharField,
            'year': django_fields.IntegerField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your UserProfileForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field '{expected_field_name}' in UserProfileForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")
    

    
    