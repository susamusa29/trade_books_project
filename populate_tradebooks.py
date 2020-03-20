import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trade_books_project.settings')

import django
django.setup()
from tradebooks.models import Book, UserProfile, Payment

def populate():
    # Creating the data

    books = [{  'ISBN':'9780435910105',  
                'bookID':1,
                'bookImage':'/ddd.jpg',
                'bookName': "Opening Spaces: An Anthology of Contemporary African Women's Writing",
                'bookAuthor':"Yvonne Vera",
                'course':'BSc Compuring Science',
                'year':1,
                'bookDescription':"slightly used, but in good condition"
                }]

    
    #takes all the books and adds them.

    for b in books :
        add_book(b['bookID'], b['bookImage'], b['bookName'], b['bookAuthor'], b['course'], b['year'], b['bookDescription'], b['ISBN'])
  
    #Code to add a book

def add_book(id, image, title, author, course, year, descr, isbn):
    b = Book.objects.get_or_create(bookID = id, bookName = title)[0]
    b.bookImage = image
    b.bookAuthor = author
    b.course = course
    b.year = year
    b.bookDescription = descr
    b.bookISBN = isbn
    b.save()
# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
