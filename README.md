# Django Register app
  This is a school register api, that enables creating records of students who are absent or present.

# Dependencies:
    Django - The backbone upon which this REST API is built upon. It's a Python web framework that features models, views, url routes and user management among many other features.

    Django REST framework - This is a powerful and flexible toolkit for building browsable REST APIs. It includes support for model serialization, permissions (default and custom) and viewsets among other features.

# Features:
*  CRUD for school, teacher, level, register, student.
*  Retrieve a list of all registers.
*  Bulk create a list of students

## Usage:

* Clone the repo: git@github.com:penny-wanjiru/School_register.git

* Install requirements.
 `pip install -r requirements.txt`

* Install the project's database. SQlite was used for this checkpoint.

* Perform database migrations.
    `python manage.py makemigrations `
    `python manage.py migrate `

* Run the application
 `python manage.py runserver`


## Testing
To run tests:
`python manage.py test`

## TO DO:
* Add CI for the project
* Bulk create for register
* Add more tests
