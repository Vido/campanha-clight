#!/home/scholarisadmin/public_html/clight/env34/bin/python

"""
WSGI config for campanha_clight project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import sys
sys.path.insert(0,
   '/home/scholarisadmin/public_html/clight/campanha-clight/campanha_clight/')

import os
os.environ.setdefault('PYTHONPATH', 
   '/home/scholarisadmin/public_html/clight/campanha-clight/campanha_clight/'
)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campanha_clight.settings')

#application = get_wsgi_application()
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method='threaded', deamonize='false')
