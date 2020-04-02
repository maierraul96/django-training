"""
WSGI config for django_training project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

project_folder = os.path.abspath(os.path.join(__file__, "../../.."))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_training.settings')
load_dotenv(os.path.join(project_folder, '.env.dev'))

application = get_wsgi_application()
