Make sure you have django >=1.7 installed, run

    python -c "import django; print(django.get_version())"

To check.

This also assumes you're using a unix style cli, so Linux / MacOS X

To start, run the following commands:

    python manage.py migrate

    python manage.py shell < seed_script.py

To setup the SQLite database

Then to run use:

    python manage.py runserver

Then go to 

    http://localhost:8000

Some default users have been set up.  Try any of the following:

    john
    joan
    suzy
    billy

With the password (same for all with the default users)

    abc123

Use the input box on the bottom to add new items, click on an item to edit or delete it.

I didn't build up CRUD forms for users, but the django admin works.  You just have to create a superuser:

    python manage.py createsuperuser

Then go to 

    http://localhost:8000/admin
