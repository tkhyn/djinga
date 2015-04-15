"""
Jinja2 template loaders for use in Django < 1.8
"""

import jinja2

from django.template import loader
from django.template.loaders import app_directories, filesystem
from django.conf import settings

from .environment import Environment

_env = None


def _init_env():
    """
    Initialise the environment that is going to be used in the loaders
    """
    if _env:
        return

    template_dirs = [x for ldr_str in settings.TEMPLATE_LOADERS\
        for x in loader.find_template_loader(ldr_str)\
                       .get_template_sources('')]

    options = dict(
        loader=jinja2.FileSystemLoader(template_dirs),
        extensions=set(kwargs.get('extensions', [])) \
            .union(getattr(settings, 'JINJA2_EXTENSIONS', {}))
    )

    options.update(getattr(settings, 'JINJA2_ENV_ARGS', {}))

    _env = Environment(**options)

    _env.filters.update(getattr(settings, 'JINJA2_FILTERS', {}))
    _env.globals.update(getattr(settings, 'JINJA2_GLOBALS', {}))


class DjingaLoaderBase(object):
    """
    Overrides django default template loader with Jinja2 depending on a
    user-defined condition (function returning a boolean)

    Also creates a jinja2 environment linked to this loader
    """

    def __init__(self, *args, **kwargs):
        _init_env()

    def load_template(self, template_name, template_dirs=None):

        if _env.use_jinja(template_name):
            return _env.get_template(template_name)

        return super(DjingaLoaderBase, self). \
            load_template(template_name, template_dirs)


class FileSystemLoader(DjingaLoaderBase, filesystem.Loader):
    pass


class AppLoader(DjingaLoaderBase, app_directories.Loader):
    pass
