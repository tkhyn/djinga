import django
from django import test
from django.template.loader import get_template
from django.template import Context
from django.test.client import RequestFactory
from django.test.utils import override_settings

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
        self.request = RequestFactory().get('/')

    def setEnvironment(self, **kwargs):
        if django.VERSION < (1, 8):
            cps = kwargs.pop('context_processors', ())
            self._override_settings = override_settings(
                TEMPLATE_CONTEXT_PROCESSORS=cps)
            self._override_settings.enable()
        set_environment(**kwargs)

    def _post_teardown(self):
        try:
            self._override_settings.disable()
        except AttributeError:
            pass
        self.setEnvironment(**self.old_options)
        super(TestCase, self)._post_teardown()

    def render(self, **context):
        if self.template_file:
            tmpl = get_template(self.template_file)
            context = Context(context)
        else:
            tmpl = engines['djinga'].from_string(self.template)
        try:
            return tmpl.render(context, self.request)
        except TypeError:
            # django < 1.8
            context['request'] = self.request
            return tmpl.render(context)

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
