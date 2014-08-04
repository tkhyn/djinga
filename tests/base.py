from django.utils import unittest
from django.template.loader import get_template
from django.template import Context

from djinga import environment
from djinga import loaders


# nose should not look for tests in this module
__test__ = False
__unittest = True


class TestEnvMetaClass(environment.EnvMetaClass):
    __test__ = False

    def __call__(self, *args, **kw):
        self.instance = type.__call__(self, *args, **kw)
        loaders.env = self.instance
        return self.instance


class TestEnvironment(environment.Environment):
    __test__ = False
    __metaclass__ = TestEnvMetaClass


class TestCase(unittest.TestCase):

    extensions = ()
    template = ''
    template_file = ''

    def setUp(self):
        self.env = TestEnvironment(extensions=self.extensions)

    def render(self, **context):
        if self.template_file:
            tmpl = get_template(self.template_file)
            context = Context(context)
        else:
            tmpl = self.env.from_string(self.template)
        return tmpl.render(context)

    def assertRender(self, expected, context={}, msg=None):
        actual = self.render(**context)
        self.assertEqual(actual, expected, msg)
