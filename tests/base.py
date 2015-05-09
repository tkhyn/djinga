from django import test
from django.template.loader import get_template
from django.template import Context
from django.test.client import RequestFactory

from djinga.engines import engines

from .compat import set_environment, get_old_options


# nose should not look for tests in this module
__test__ = False
__unittest = True


class TestCase(test.TestCase):

    options = None
    template = ''
    template_file = ''

    def _pre_setup(self):
        super(TestCase, self)._pre_setup()
        self.old_options = get_old_options()
        self.setEnvironment(**(self.options or {}))

    def setEnvironment(self, **kwargs):
        set_environment(**kwargs)

    def _post_teardown(self):
        self.setEnvironment(**self.old_options)
        super(TestCase, self)._post_teardown()

    def render(self, **context):
        request = RequestFactory().get('/')
        if self.template_file:
            tmpl = get_template(self.template_file)
            context = Context(context)
        else:
            tmpl = engines['djinga'].from_string(self.template)
        return tmpl.render(context, request)

    def assertRender(self, expected, context={}, msg=None):
        actual = self.render(**context)
        self.assertEqual(actual, expected, msg)


class ExtTestCase(TestCase):

    extensions = ()

    def _pre_setup(self):
        self.options = self.options or {}
        try:
            self.options['extensions'] += self.extensions
        except KeyError:
            self.options['extensions'] = self.extensions
        super(ExtTestCase, self)._pre_setup()
