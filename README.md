<p align="center">
    <a href="http://desuderata.pythonanywhere.com">
      <h1 style="color:rgb(119,179,212);">
        <img src="/static/images/tradebooklogo.png"
             alt="TradeBooks Logo"
             width="64"
             height="64">
        Trade<span style="color:rgb(199,92,92);">Books</span>
      </h1>
    </a>
</p>

# Tradebooks

Tradebooks is a webpage that aids students in buying and selling used books. The site hopes to help students who may be less financially fortunate to get the books they require, as well as graduating students who may no longer need their books.

The site is currently up at: [http://desuderata.pythonanywhere.com/](http://desuderata.pythonanywhere.com/)

## Prerequisites

The website is built on:

[Python 3.7](https://www.python.org/downloads/release/python-370/)

[Django 2.2.3 (LTS)](https://docs.djangoproject.com/en/3.0/releases/2.2.3/)

[Bootstrap 4](https://getbootstrap.com/)

[JQuery](https://jquery.com/)

[AJAX](https://api.jquery.com/category/ajax/)


## Installation

The repository of our webpage could be found here: [https://github.com/susamusa29/trade_books_project/](https://github.com/susamusa29/trade_books_project/)

1. Create a virtual environment:
```bash
conda create -n tradebooks python=3.7.2
conda acitivate tradebooks
```

2. Clone our repository:
```bash
git clone https://github.com/susamusa29/trade_books_project/
```

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages:
```bash
pip install -r requirements.txt
```

4. Migrate database models:
```bash
cd trade_books_project
py manage.py makemigrations tradebooks
py manage.py migrate
```

5. Run the population script to populate the database for testing.
Note: python is used as "py " will not work and causes an error.
```bash
python population_script.py
```

6. Run the server
```bash
py manage.py runserver
```

## Unit Testing

To run a unit test
```bash
python manage.py test <test-file-name>
```

We have a total of five unit tests:

- tests
- tests_2
- tests_3
- tests_4,7
- tests_5,8

Run the code five times, replacing <test-file-name> with the name of the unit test file.

Note: Omit the file extension ".py" when unit testing.

## Usage

Five accounts are added by the population script, namely:
- desuderata
- okiTACObigtaco
- susamusa29
- abrar928
- NoobMaster69.

with "password" being the password for all five.
### Register as a user
To register as a user, simply navigate to the register page to create an account. After creating an account, you could now log in to start trading books.

### Adding a listing

To add a listing, navigate to your profile page then click on "add a listing" in the listing section of your page. You will be redirected to the add a listing page to add a book to sell.

### Remove a listing

If you created a listing by mistake, changed your mind or perhaps, sold your book, you could delete a listing on the listing section of your profile. Simply click on the delete link below and you will be redirected to a webpage to confirm you actions. In addition, you could navigate to your listing page to delete your listing.

**Important**: If you would like to delete your book from our catalog, check the option to do so. Otherwise, you will have to contact our staff through the contact us page to request for a deletion.

### Buy a book

To buy a book, you must be logged in. Navigate to the all books/listing page to search for a book, or use the searchbar to search for a book by title, ISBN, author or course. To search for more than one field, please ensure that there is a space between your search keywords.

After finding your desired book, you should be able to contact the seller through the "Contact Seller" button. You will be redirected to your email app to liaise with the seller. To purchase, click the "Purchase This!" and you should receive a confirmation email from us.

### Other user actions
Most user actions could be found in your profile page. You could edit your profile and change your password there.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and Contact
Teoh Yee Hou ([desuderata](https://github.com/desuderata)) - [2471020t@student.gla.ac.uk](2471020t@student.gla.ac.uk)

Stanislava Dyakova ([susamusa29](https://github.com/susamusa29)) - [2390717d@student.gla.ac.uk](2390717d@student.gla.ac.uk)

Abrar Haroon ([Abrar-Haroon](https://github.com/abrar-haroon))- [2513933h@student.gla.ac.uk](2513933h@student.gla.ac.uk)

## Acknowledgements
[Make a README](https://www.makeareadme.com/)

[Font Awesome](https://fontawesome.com/)

[Tango With Django](https://github.com/maxwelld90/tango_with_django_2_code)

[SMTPlib](https://docs.python.org/3/library/smtplib.html)

[StackOverflow](https://stackoverflow.com/)

[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
