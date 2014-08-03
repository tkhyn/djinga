
# nose should not look for tests in this module
__test__ = False

from django.utils import unittest

from djinga import environment


class TestEnvMetaClass(environment.EnvMetaClass):
    __test__ = False

    def __call__(self, *args, **kw):
        self.instance = type.__call__(self, *args, **kw)
        return self.instance


class TestEnvironment(environment.Environment):
    __test__ = False
    __metaclass__ = TestEnvMetaClass


class TestCase(unittest.TestCase):

    extensions = ()
    template = ''

    def setUp(self):
        self.env = TestEnvironment(extensions=self.extensions)

    def render(self, **context):
        tmpl = self.env.from_string(self.template)
        return tmpl.render(context)
