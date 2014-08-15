from django.test.utils import override_settings
from django.core.exceptions import ImproperlyConfigured

from .base import TestCase, TestEnvironment


class DjangoTemplateFileExtTests(TestCase):

    extensions = ('djinga.ext.static',
                  'djinga.ext.url')

    @override_settings(JINJA2_JJ_EXTS=('.jinja',))
    def test_single_filext(self):
        self.env = TestEnvironment(extensions=self.extensions)
        self.template_file = 'file_exts/jinja.jinja'
        self.assertRender('/not_found/\n'
                          '/static/css')

    @override_settings(JINJA2_JJ_EXTS='jinja')
    def test_filext_as_string(self):
        with self.assertRaises(ImproperlyConfigured):
            self.env = TestEnvironment(extensions=self.extensions)
