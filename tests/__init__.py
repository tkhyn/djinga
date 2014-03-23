# Django settings must be configured before anything is imported from djinga
# package. It is therefore necessary to do it there, at the import level and
# before any test module is imported, and not in a setup_package function


import os
import sys

from django.conf import settings as dj_settings
from .settings import SETTINGS

dj_settings.configure(**SETTINGS)
