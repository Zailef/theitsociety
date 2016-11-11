from __future__ import absolute_import, unicode_literals

from .base import *

import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['138.68.137.83']

try:
    from .local import *
except ImportError:
    pass
