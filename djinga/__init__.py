from .version import __version__, __version_info__
from .environment import env

from django.template import add_to_builtins
add_to_builtins('djinga.templatetags.djinga_tags')
