import subprocess
from doit.tools import LongRunning
def task_pip_install():
    """ install requirements """
    return {
        'actions': ['pip install -r requirements.txt']
    }

def task_export_env_vars():
    """ env setup """
    def set_env_vars():
        try:
            env = open(file='.env', mode = 'x')
            
            env.write("SECRET_KEY=!eep#0++x*bvn&x49+31t@_=09j#+-49q)wafyym&9_nhrzaks\nSDDTF_USER=sdNd\nSDDTF_PASS=mongo123")

        except FileExistsError:
            pass

    return {
        'actions' : [set_env_vars]
    }

def task_db_install():
    """Installing postgreSQL dependencies"""
    def create_db():
        try:
            stream = subprocess.call(['createdb', 'test_db', '-U postgres'],shell=True)
            
        except:
            print('failure')
            pass
    
    return{
        'actions' : ["sudo apt-get install postgresql",create_db]
    }

def task_migrations():
    """ making migrations """
    
    return {
        'actions' : ['python manage.py makemigrations','python manage.py migrate']
    }
def print_instruc():
        print("Enter 'yes' ")    
def task_static():
    """ collect django prebaked static files """
    
    
    return { 
        'actions' : [print_instruc,'python manage.py collectstatic']
    }
def task_superuser():
    """ create super user command for admin """
    return {
        'actions' : ['python manage.py createsuperuser']
    }
def task_dock():
    """ docker redis server """
    return {
        'actions' : ['sudo docker run -p 6379:6379 -d redis:5']
    }
def task_runserver():
    """ django runserver """
    cmd = 'python manage.py runserver'
    return {'actions' : [LongRunning(cmd)]}