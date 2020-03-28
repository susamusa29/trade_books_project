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
                },
                {'ISBN':'186914001X',  
                'bookID':2,
                'bookImage':'/ddd.jpg',
                'bookName': "MIPS Assembly Language Programming using QtSpim",
                'bookAuthor':"Ed Jorgensen",
                'course':'BSc Compuring Science',
                'year':3,
                'bookDescription':"The purpose of this text is to provide a simple and free \
                reference for university level programming and architecture units that include a brief section covering \
                MIPS assembly language programming. The text assumes usage of the QtSpim simulator."
                },
                {  'ISBN':'9781558614062',  
                'bookID':3,
                'bookImage':'/ddd.jpg',
                'bookName': "God Created the Integers",
                'bookAuthor':"Hawking, Stephen",
                'course':'BSc Mathematics',
                'year':4,
                'bookDescription':"slightly used, but in good condition. Book about Maths."
                },
                {  'ISBN':'1594606471',  
                'bookID':4,
                'bookImage':'/ddd.jpg',
                'bookName': "Integration of the Indian States",
                'bookAuthor':"Menon, V P",
                'course':'MSc History',
                'year':2,
                'bookDescription':"not used, brand new"
                },
                {  'ISBN':'0869809180',  
                'bookID':5,
                'bookImage':'/ddd.jpg',
                'bookName': "Wealth of Nations, The",
                'bookAuthor':"Smith, Adam",
                'course':'BSc Economics',
                'year':2,
                'bookDescription':"slightly used, but in good condition. The cover page is missing."
                },{  'ISBN':'006059537X',  
                'bookID':6,
                'bookImage':'/ddd.jpg',
                'bookName': "Return of the Primitive",
                'bookAuthor':"Rand, Ayn",
                'course':'BSc Psychology',
                'year':3,
                'bookDescription':"slightly used, but in good condition"
                },{  'ISBN':'0547241607',  
                'bookID':7,
                'bookImage':'/ddd.jpg',
                'bookName': "Data Structures Using C & C++",
                'bookAuthor':"Tanenbaum, Andrew",
                'course':'BSc Compuring Science',
                'year':3,
                'bookDescription':"slightly used, but in good condition"
                },
                {  'ISBN':'9780939691029',  
                'bookID':8,
                'bookImage':'/ddd.jpg',
                'bookName': "Trial, The",
                'bookAuthor':"Kafka, Frank",
                'course':'BSc Classics',
                'year':4,
                'bookDescription':"in good condition"
                },
                {  'ISBN':'044657922X',  
                'bookID':9,
                'bookImage':'/ddd.jpg',
                'bookName': "Tao of Physics, The",
                'bookAuthor':"Capra, Fritjof",
                'course':'BSc Physics',
                'year':2,
                'bookDescription':"slightly used, but in good condition"
                },
                {  'ISBN':'0939691027',  
                'bookID':10,
                'bookImage':'/ddd.jpg',
                'bookName': "Age of Discontuinity, The",
                'bookAuthor':"Drucker, Peter",
                'course':'BSc Economics',
                'year':3,
                'bookDescription':"slightly used"
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
