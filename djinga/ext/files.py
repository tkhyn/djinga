"""
Extensions to serve static and media files
"""

from jinja2 import nodes
from jinja2.ext import Extension

from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings as dj_settings


class SimpleTag(Extension):
    """
    Base class for a simple tag returning a constant string
    """
    abstract = True

    def parse(self, parser):
        parser.stream.next()
        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
        return nodes.Output([self.call_method('tag_func', args)])


class StaticExtension(SimpleTag):
    """Django-like static tag"""
    tags = set(['static'])

    def tag_func(self, path):
        return staticfiles_storage.url(path)


class StaticCSSExtension(SimpleTag):
    tags = set(['css'])

    def tag_func(self, path):
        return '<link rel="stylesheet" type="text/css" href="%s">' % \
            staticfiles_storage.url('%s/%s.css' % \
                                    (self.environment.css_dir, path))


class StaticJSExtension(SimpleTag):
    tags = set(['js'])

    def tag_func(self, path):
        return '<script type="text/javascript" src="%s"></script>' % \
            staticfiles_storage.url('%s/%s.js' % \
                                    (self.environment.js_dir, path))


class MediaExtension(SimpleTag):
    tags = set(['media'])

    def tag_func(self, path):
        return dj_settings.MEDIA_URL + path
