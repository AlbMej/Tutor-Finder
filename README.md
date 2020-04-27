# Tutor Finder

Tutor Finder is a web app which allows students to find tutors for classes as well as register and make money as a tutor.

## Setup
Make sure to have Python3 & venv installed.
Note that everything uses python3, if that is not your default version of python use *python3* in place of python and *pip3* in place of pip.
Reference: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

1. Create the virtual enviroment (as explained in link above)
2. Activate the enviroment (as explained in link above)
3. Install the dependencies via `pip install -r requirements.txt`

### Setting up .env

Tutor Finder expects the following variables to exist within the environment:  
SECRET_KEY  

Create a file titled *.env* and save at the top level (Tutor-Finder folder).

A example/testing .env file could look like  
`SECRET_KEY='yOuR_sEcReCt_KeY'`

## Database Setup/Reset

Any changes to the models will result in a database change. The DATABASE_URL environment variable should be set up already by Heroku Postgres.
However, locally you need PostgreSQL installed. You can have dj_database_url fall back to SQLite but it's strongly recommended to use the same database engine in all of your environments.
You don't want to have your code work locally with SQLite, but fail in production with PostgreSQL.

1. Command for Ubuntu to install postgresql: `sudo apt-get install postgresql`
2. Use the OS user postgres to create the database, enter: `sudo -u postgres -i` (opens another terminal)
3. Create a database named test_db by the user postgres: `psql -c 'create database test_db;' -U postgres`
4. Exit the postgres terminal (CTRL+D).
4. Run `python manage.py makemigrations`
5. Run `python manage.py migrate`

## Docker for chat

To use the chat feature, you need a docker running. In Ubuntu, this command should do the trick: `sudo docker run -p 6379:6379 -d redis:5`

## Launching the server
1. python manage.py runserver
2. Using the web browser of your choice go to `localhost:8000` (check list of supported browsers)
3. Quit the server with CONTROL-C

## closing the virtual environment
1. deactivate

## Common errors

1. (For Ubuntu) If you ever get an error asking "Is the server running locally and accepting connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?"
Start the server with `sudo service postgresql start`. You can also stop the server with `sudo service postgresql stop`.

2. If you get a "no password supplied" error, go into your pg_hba.conf file where ever it is located and change md5/peer to trust in the local line/s. For example mine was:
`sudo nano /etc/postgresql/10/main/pg_hba.conf`
Then restart the server with: `sudo /etc/init.d/postgresql restart`

3. If you get a "psql: FATAL:  Peer authentication failed for user "postgres" error, try: `sudo -u postgres psql -c 'create database test_db;' -U postgres`
OR go back into the pg_hba.conf file and md5/peer to trust in the host line/s.

4. If you are really desperate and nothing works try setting all the lines to trust.
