from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hlox6gzg2l=l#qi1lo948s_1fjz65^mpl1z@wf=q&=se=5oe0b'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['138.68.137.83', 'theitsociety.com']


try:
    from .local import *
except ImportError:
    pass
