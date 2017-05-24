**About Will Legislate For Money**

Will Legislate For Money is a Python/Django app built as a tool to give voters easier access to information on their legislators’ campaign funding and congressional action.

You can use the live site at http://legislate.money

**Setup**

If you are new to Python/Django, you can use this guide to help set up your environment:

    http://www.obeythetestinggoat.com/book/pre-requisite-installations.html

Will Legislate For Money uses Python 3 and Django 1.11rc1.

Clone down this repo.

Dependencies:

In your virtual environment, install:

    requests
    
		shutil

To set up the database and seed data:

    python manage.py migrate
    python manage.py seed_legislators

**Usage**

Note: To run the test suite, you will need to install vcrpy and selenium>3.

To run the tests:

		python manage.py test

To run the server (runs on port 8000):

		python manage.py runserver

To get into the database shell (if you work in the shell, you have to import the models in order to use the ORM):

    python manage.py dbshell

**Third-Party APIs**

Will Legislate For Money uses multiple APIs to get information on legislators.
The Industry Contributions and Organization Contributions are populated by the OpenSecrets API (https://www.opensecrets.org/resources/create/api_doc.php).

The Sponsored Bills and Recent Decisions are populated by the Pro Public congressional API (https://projects.propublica.org/api-docs/congress-api/).

The Recent Bills are populated by the govtrack API (http://govtrack.us/api).

The list of legislators is populated by the Sunlight Foundation (https://congress.api.sunlightfoundation.com/legislators).
