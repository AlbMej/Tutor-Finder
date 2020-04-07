from .settings import * #Import base settings
from decouple import config
DEBUG = False
ADMINS = [('Alberto Mejia', 'albertomejia295@gmail.com')]

# SDDTF_USER = config('SDDTF_USER') # Removed MongoDB, Only need dj_database_url()
# SDDTF_PASS = config('SDDTF_PASS') # in base settings for Heroku Postgres 

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