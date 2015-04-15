from django.core.exceptions import ImproperlyConfigured

from .base import TestCase


class DjangoTemplateFileExtTests(TestCase):

    extensions = ('djinga.ext.static',
                  'djinga.ext.url')

    def test_single_filext(self):
        self.setEnvironment(jj_exts=('jinja',), extensions=self.extensions)
        self.template_file = 'file_exts/jinja.jinja'
        self.assertRender('/not_found/\n'
                          '/static/css')

    def test_filext_as_string(self):
        with self.assertRaises(ImproperlyConfigured):
            self.setEnvironment(jj_exts='jinja',
                                extensions=self.extensions)
