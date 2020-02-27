from .settings import * #Import base settings
from decouple import config
DEBUG = False
ADMINS = [('Alberto Mejia', 'albertomejia295@gmail.com')]

# SDDTF_USER = os.environ['SDDTF_USER']  #<-- Similarly, use this if you store your SDDTF/Mongo username as an environment variable
# SDDTF_PASS = os.environ['SDDTF_PASS']  #<-- Same thing for password
SDDTF_USER = config('SDDTF_USER')
SDDTF_PASS = config('SDDTF_PASS')

DATABASES = { 
    'default': {
        'ENGINE'  : 'djongo',
        'NAME'    : 'SDDTF', 
        'HOST'    : f'mongodb+srv://{SDDTF_USER}:{SDDTF_PASS}@tutor-finder-dbs-ayohv.mongodb.net/test?retryWrites=true&w=majority',
        'USER'    : SDDTF_USER,
        'PASSWORD': SDDTF_PASS,
    }
}

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage' #This alias has now been removed as per the 4.0 update.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['sdd-tutor-finder.herokuapp.com', '127.0.0.1', 'localhost']