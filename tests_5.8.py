
# run $ python manage.py test tradebooks.tests_5.8
# 
# The tests will then be run, and the output displayed -- do you pass them all?
# 
# Once you are done with the tests, delete the module. You don't need to put it in your Git repository!
#

import os
import re
import inspect
from tradebooks.models import UserProfile, Book
from populate_tradebooks import populate
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class TemplateTests(TestCase):
    """
    I don't think it's possible to test every aspect of templates from this chapter without delving into some crazy string checking.
    So, instead, we can do some simple tests here: check that the base template exists, and that each page in the templates/tradebooks directory has a title block.
    Based on the idea by Gerardo -- beautiful idea, cheers big man.
    """
    def get_template(self, path_to_template):
        """
        Helper function to return the string representation of a template file.
        """
        f = open(path_to_template, 'r')
        template_str = ""

        for line in f:
            template_str = f"{template_str}{line}"

        f.close()
        return template_str
    
    def test_base_template_exists(self):
        """
        Tests whether the base template exists.
        """
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'tradebooks', 'base.html')
        self.assertTrue(os.path.exists(template_base_path), f"{FAILURE_HEADER}We couldn't find the new base.html template that's required in the templates/tradebooks directory. Did you create the template in the right place?{FAILURE_FOOTER}")
    
    
    def test_template_usage(self):
        """
        Check that each view uses the correct template.
        """
        populate()
        
        urls = [reverse('tradebooks:about'),
                reverse('tradebooks:add_book'),
                reverse('tradebooks:books'),
                reverse('tradebooks:index'),]

        templates = ['tradebooks/about.html',
                     'tradebooks/add_book.html',,
                     'tradebooks/books.html',
                     'tradebooks/index.html',]
        
        for url, template in zip(urls, templates):
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)

    
    
    def test_for_links_in_base(self):
        """
        There should be three hyperlinks in base.html, as per the specification of the book.
        Check for their presence, along with correct use of URL lookups.
        """
        template_str = self.get_template(os.path.join(settings.TEMPLATE_DIR, 'tradebooks', 'base.html'))

        look_for = [
            '<a href="{% url \'tradebooks:add_book\' %}">Add a New Category</a>',
            '<a href="{% url \'tradebooks:about\' %}">About</a>',
            '<a href="{% url \'tradebooks:index\' %}">Index</a>',
        ]
        
        for lookup in look_for:
            self.assertTrue(lookup in template_str, f"{FAILURE_HEADER}In base.html, we couldn't find the hyperlink '{lookup}'. Check your markup in base.html is correct and as written in the book.{FAILURE_FOOTER}")