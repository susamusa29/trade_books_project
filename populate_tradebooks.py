"""Population script.

Note:
added population for user(Teoh)

todo:
polish population script

author: Stanislava Dyakova (2390717d)
        Teoh Yee Hou (2471020t)

"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trade_books_project.settings')

import django

django.setup()
from tradebooks.models import Book, UserProfile, Payment, Listing

from django.contrib.auth.models import User


def populate():
    # Creating the data

    books = [{'ISBN': '9780435910105',
                'bookID':1,
              'bookImage': 'book_images/openingSpaces.jpg',
              'bookName': "Opening Spaces: An Anthology of Contemporary African Women's Writing",
              'bookAuthor': "Yvonne Vera",
              'course': 'BSc Compuring Science',
              'year': 1,
              'bookDescription': "slightly used, but in good condition"
              },
             {'ISBN': '186914001X',
             'bookID':2,
              'bookImage': 'book_images/mips.png',
              'bookName': "MIPS Assembly Language Programming using QtSpim",
              'bookAuthor': "Ed Jorgensen",
              'course': 'BSc Compuring Science',
              'year': 3,
              'bookDescription': "The purpose of this text is to provide a simple and free \
                reference for university level programming and architecture units that include a brief section covering \
                MIPS assembly language programming. The text assumes usage of the QtSpim simulator."
              },
             {'ISBN': '9781558614062',
             'bookID':3,
              'bookImage': 'book_images/godint-wholebook.jpg',
              'bookName': "God Created the Integers",
              'bookAuthor': "Hawking, Stephen",
              'course': 'BSc Mathematics',
              'year': 4,
              'bookDescription': "slightly used, but in good condition. Book about Maths."
              },
             {'ISBN': '1594606471',
             'bookID':4,
              'bookImage': 'book_images/indianstates.jpg',
              'bookName': "Integration of the Indian States",
              'bookAuthor': "Menon, V P",
              'course': 'MSc History',
              'year': 2,
              'bookDescription': "not used, brand new"
              },
             {'ISBN': '0869809180',
             'bookID':5,
              'bookImage': 'book_images/wealthnations.jpg',
              'bookName': "Wealth of Nations, The",
              'bookAuthor': "Smith, Adam",
              'course': 'BSc Economics',
              'year': 2,
              'bookDescription': "slightly used, but in good condition. The cover page is missing."
              },
             {'ISBN': '006059537X',
             'bookID':6,
              'bookImage': 'book_images/primitive.jpg',
              'bookName': "Return of the Primitive",
              'bookAuthor': "Rand, Ayn",
              'course': 'BSc Psychology',
              'year': 3,
              'bookDescription': "slightly used, but in good condition"
              },
             {'ISBN': '0547241607',
             'bookID':7,
              'bookImage': 'book_images/datastr.jpg',
              'bookName': "Data Structures Using C & C++",
              'bookAuthor': "Tanenbaum, Andrew",
              'course': 'BSc Compuring Science',
              'year': 3,
              'bookDescription': "slightly used, but in good condition"
              },
             {'ISBN': '9780939691029',
             'bookID':8,
              'bookImage': 'book_images/trial.jpg',
              'bookName': "Trial, The",
              'bookAuthor': "Kafka, Frank",
              'course': 'BSc Classics',
              'year': 4,
              'bookDescription': "in good condition"
              },
             {'ISBN': '044657922X',
             'bookID':9,
              'bookImage': 'book_images/pyhsicstoa.jpg',
              'bookName': "Tao of Physics, The",
              'bookAuthor': "Capra, Fritjof",
              'course': 'BSc Physics',
              'year': 2,
              'bookDescription': "slightly used, but in good condition"
              },
             {'ISBN': '0939691027',
             'bookID':10,
              'bookImage': 'book_images/disc.jpg',
              'bookName': "Age of Discontuinity, The",
              'bookAuthor': "Drucker, Peter",
              'course': 'BSc Economics',
              'year': 3,
              'bookDescription': "slightly used"
              }]

    users = [{"username": "desuderata",
              "studentNumber": "2471020T",
              "firstName": "Yee Hou",
              "lastName": "Teoh",
              "email": "2471020t@student.gla.ac.uk",
              "profilePicture": "profile_images/EBB7vnxU0AA_Tw-.jpg",
              "courseMain": "Computing Science",
              "year": "2"},
             {"username": "susamusa29",
              "studentNumber": "2390717D",
              "firstName": "Stanislava",
              "lastName": "Dyakova",
              "email": "2390717d@student.gla.ac.uk",
              "profilePicture": "profile_images/noobmaster69.jpg",
              "courseMain": "Computing Science",
              "year": "2"},
             {"username": "abrar928",
              "studentNumber": "2513933H",
              "firstName": "Abrar",
              "lastName": "Haroon",
              "email": "2513933H@student.gla.ac.uk",
              "profilePicture": "profile_images/abrar.jpg",
              "courseMain": "Computing Science",
              "year": "2"},
             {"username": "NoobMaster69",
              "studentNumber": "2345678D",
              "firstName": "John",
              "lastName": "Doe",
              "email": "2345678d-fake@student.gla.ac.uk",
              "profilePicture": "profile_images/7b9.jpg",
              "courseMain": "Engineering",
              "year": "4"},
             ]

    userlist = [add_user(u['username'],
                 u['studentNumber'],
                 u['firstName'],
                 u['lastName'],
                 u['email'],
                 u['profilePicture'],
                 u['courseMain'],
                 u['year'], ) for u in users]

    booklist = [add_book(b['bookID'],
                 b['bookImage'],
                 b['bookName'],
                 b['bookAuthor'],
                 b['course'],
                 b['year'],
                 b['bookDescription'],
                 b['ISBN']) for b in books]
    listings = [{"user":userlist[3],
                "bookName":"God Created the Integers",
                "description":"slightly used, but in good condition. Book about Maths.",
                "price":42,
                },
                {"user": userlist[0],
                 "bookName": "MIPS Assembly Language Programming using QtSpim",
                 "description": "slightly used, but in good condition.",
                 "price": 69,
                 },
                {"user": userlist[0],
                 "bookName": "God Created the Integers",
                 "description": "heavily used. pages that fell out have been taped together",
                 "price": 17,
                 },
                {"user": userlist[1],
                 "bookName": "Wealth of Nations, The",
                 "description": "slightly used, but in good condition.",
                 "price": 70,
                 },
                {"user": userlist[2],
                 "bookName": "Return of the Primitive",
                 "description": "First listing... hope its up",
                 "price": 13,
                 },

                ]

    # takes all the books and adds them.

    for b in books:
        add_book(b['bookID'],
                 b['bookImage'],
                 b['bookName'],
                 b['bookAuthor'],
                 b['course'],
                 b['year'],
                 b['bookDescription'],
                 b['ISBN'])

    # teoh: populate users

    for u in users:
        add_user(u['username'],
                 u['studentNumber'],
                 u['firstName'],
                 u['lastName'],
                 u['email'],
                 u['profilePicture'],
                 u['courseMain'],
                 u['year'], )

    # teoh: populate listings
    for l in listings:
        add_listing(l['user'],
                    l['bookName'],
                    l['description'],
                    l['price'],)



# Code to add a book

def add_book(id, image, title, author, course, year, descr, isbn):
    b = Book.objects.get_or_create(bookID=id, bookName=title)[0]
    b.bookImage = image
    b.bookAuthor = author
    b.course = course
    b.year = year
    b.bookDescription = descr
    b.bookISBN = isbn
    b.save()


def add_user(username, student_number, first_name, last_name, email,
             profile_picture, course_main, year):
    user = User.objects.get_or_create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )[0]
    user.set_password('password')

    user.save()
    user_profile = UserProfile.objects.get_or_create(
        user=user,
        picture=profile_picture,
        courseMain=course_main,
        year=year,
        studentID=student_number)[0]
    user_profile.save()
    return user_profile


def add_listing(username, bookname, description, price):
    listing = Listing.objects.get_or_create(
        user=username,
        info=description,
        price=price,
        book=bookname,
    )[0]
    listing.save()

    return listing


# Start execution here!
if __name__ == '__main__':
    print('Starting Tradebooks population script...')
    populate()
