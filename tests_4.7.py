# 
# Tango with Django 2 Progress Tests
# By Leif Azzopardi and David Maxwell
# With assistance from Enzo Roiz (https://github.com/enzoroiz) and Gerardo A-C (https://github.com/gerac83)
# 
# Chapter 7 -- Forms
# Last updated: January 7th, 2020
# Revising Author: David Maxwell
# 

#
# In order to run these tests, copy this module to your tango_with_django_project/tradebooks/ directory.
# Once this is complete, run $ python manage.py test tradebooks.tests_chapter7
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

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
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
            resolved_name = resolve('/tradebooks/add_book/').view_name
        except:
            resolved_name = ''
        
        self.assertEqual(resolved_name, 'tradebooks:add_book', f"{FAILURE_HEADER}The lookup of URL '/tradebooks/add_book/' didn't return a mapping name of 'tradebooks:add_book'. Check you have the correct URL mapping for adding a Book, and try again.{FAILURE_FOOTER}")
    
    def test_index_link_added(self):
        """
        Checks whether a link has been added as required on the index UserProfile, taking a user to the add Book UserProfile.
        """
        response = self.client.get(reverse('tradebooks:index'))
        content = response.content.decode()

        self.assertTrue('<a href="/tradebooks/add_book/">Add a New Book</a><br />' in content)

    def test_add_book_template(self):
        """
        Checks whether a template was used for the add_book() view.
        """
        response = self.client.get(reverse('tradebooks:add_book'))
        self.assertTemplateUsed(response, 'tradebooks/add_book.html', f"{FAILURE_HEADER}The add_book.html template is not used for the add_book() view. The specification requires this.{FAILURE_FOOTER}")

    def test_add_book_form_response(self):
        """
        Checks the response from the initial add Book response (i.e. check the UserProfile/form is correct).
        """
        response = self.client.get(reverse('tradebooks:add_book'))
        context = response.context
        content = response.content.decode()

        self.assertTrue('form' in context)

        self.assertTrue('<h1>Add a Book</h1>' in content, f"{FAILURE_HEADER}Couldn't find 'Add a Book' header in the add_book() response. Check the template add_book.html.{FAILURE_FOOTER}")
        self.assertTrue('name="name"' in content, f"{FAILURE_HEADER}We couldn't find the form field 'name' in the rendered add_book() response. Check that your form is being created correctly.{FAILURE_FOOTER}")
        self.assertTrue('<input type="submit" name="submit" value="Create Book" />' in content, f"{FAILURE_HEADER}Couldn't find the button for 'Create Book' in the add_book() response. Check the template add_book.html.{FAILURE_FOOTER}")
        self.assertTrue('action="/tradebooks/add_book/"' in content, f"{FAILURE_HEADER}Couldn't find the correct action URL for the form in add_book.html. Check that the correct URL is provided!{FAILURE_FOOTER}")
    
    def test_add_book_functionality(self):
        """
        Adds a Book using the form, submits the request, and checks that the new Book then exists.
        """
        self.client.post(reverse('tradebooks:add_book'),
                         {'name': 'Erlang', 'views': 0, 'likes': 0})
        
        categories = Book.objects.filter(name='Erlang')
        self.assertEqual(len(categories), 1, f"{FAILURE_HEADER}When adding a new Book, it does not appear in the list of categories after being created. Check your add_book() view as the start of a debugging point.{FAILURE_FOOTER}")
    

class Chapter7UserProfileFormClassTests(TestCase):
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
            'title': django_fields.CharField,
            'url': django_fields.URLField,
            'views': django_fields.IntegerField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your UserProfileForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field '{expected_field_name}' in UserProfileForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")
    
class UserProfileFormAncillaryTests(TestCase):
    """
    Performs a series of tests to check the response of the server under different conditions when adding UserProfiles.
    """

    
    def test_register_template(self):
        """
        Checks whether a template was used for the register() view.
        """
        populate()
        response = self.client.get(reverse('tradebooks:register'))
        self.assertTemplateUsed(response, 'tradebooks/register.html', f"{FAILURE_HEADER}The register.html template is not used for the register() view. The specification requires this.{FAILURE_FOOTER}")
    
    def test_register_form_response(self):
        """
        Checks whether the template rendering register() contains a form, and whether it points to the register view.
        """
        populate()
        response = self.client.get(reverse('tradebooks:register'))
        context = response.context
        content = response.content.decode()

        self.assertTrue('<form' in content, f"{FAILURE_HEADER}We couldn't find a <form> element in the response for adding a userprofile.{FAILURE_FOOTER}")
       
    
    def test_register_bad_Book(self):
        """
        Tests whether the response for adding a userprofile when specifying a non-existent Book is per the specification.
        """
        response = self.client.get(reverse('tradebooks:register'))

        self.assertEquals(response.status_code, 302, f"{FAILURE_HEADER}When attempting to add a new user to a Book that doesn't exist, we weren't redirected. We were expecting a redirect -- check you register() view.{FAILURE_FOOTER}")
        self.assertEquals(response.url, '/tradebooks/', f"{FAILURE_HEADER}When attempting to add a new user to a Book that doesn't exist, we were not redirected to the tradebooks homeUserProfile. Check your register() view, and try again.{FAILURE_FOOTER}")

    