# Tutor Finder

Tutor Finder is a web app which allows students to find tutors
for classes as well as register and make money as a tutor.

## Setup
Make sure to have Python3 & venv installed.
Reference: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

1. Create the virtual enviroment (as explained in link above)
2. Create .env file for local user, more details below about setting up this file
3. Activate the enviroment (as explained in link above)
4. Install the dependencies via `pip install -r requirements.txt`

## Database Setup/Reset

Changes to the models will result in a database change

1. First check if a database file exists. If yes, delete that file
2. python manage.py makemigrations
3. python manage.py migrate

## Launching the server
1. python manage.py runserver
2. Using the web brower of your choice go to `localhost:8000` (check list of supported browsers)
3. Quit the server with CONTROL-C 

## closing the virtual enviroment
1. deactivate

### Setting up .env
Tutor Finder expects the following variables to exist within the enviroment
SECRET_KEY
SDDTF_USER
SDDTF_PASS

A example file could look like
'''
SECRET_KEY=mysecretkey
SDDTF_USER=myusername
SDDTF_PASS=mypassword
'''

Currently the values are not being used in a meaningful way, the values can be any non
null value