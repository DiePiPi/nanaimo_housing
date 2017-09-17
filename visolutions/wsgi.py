"""
WSGI config for visolutions project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

# gunicorn -b 0.0.0.0:8000 teaching.wsgi


import os, sys, site
from django.core.wsgi import get_wsgi_application


project = os.path.dirname(__file__)
workspace = os.path.dirname(project)

sitepackages = os.path.join(workspace, 
    'venv/local/lib64/python2.7/site-packages')
site.addsitedir(sitepackages)
projectlocation = os.path.dirname(workspace)
sys.path.append(projectlocation)
# venvactive = os.path.join(workspace, 'venv/bin/activate_this.py')
venvactive = '/home/johan/.venv/viweb/bin/activate_this.py'
# Calculate the path based on the location of the WSGI script.

sys.path.append(workspace)

# Add the path to 3rd party django application and to django itself.

os.environ['DJANGO_SETTINGS_MODULE'] = 'visolutions.settings'

if os.environ['LOCAL_SERVER_ON'] != '1':
    execfile(venvactive)

application = get_wsgi_application()
