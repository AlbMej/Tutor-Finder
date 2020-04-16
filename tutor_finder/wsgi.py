"""
WSGI config for tutor_finder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

Description:
This file is the starting page for the application to interact with
our continuouls integration server on heroku
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutor_finder.settings.heroku')

application = get_wsgi_application()
