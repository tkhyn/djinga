from django import test
from django.template.loader import get_template
from django.template import Context

from djinga.engines import engines

from .compat import set_environment, get_old_options


# nose should not look for tests in this module
__test__ = False
__unittest = True


class TestCase(test.TestCase):

    extensions = ()
    template = ''
    template_file = ''

    def _pre_setup(self):
        super(TestCase, self)._pre_setup()
        self.old_options = get_old_options()
        self.setEnvironment(extensions=self.extensions)

    def setEnvironment(self, **kwargs):
        set_environment(**kwargs)

    def _post_teardown(self):
        self.setEnvironment(**self.old_options)
        super(TestCase, self)._post_teardown()

    def render(self, **context):
        if self.template_file:
            tmpl = get_template(self.template_file)
            context = Context(context)
        else:
            tmpl = engines['djinga'].from_string(self.template)
        return tmpl.render(context)

    def assertRender(self, expected, context={}, msg=None):
        actual = self.render(**context)
        self.assertEqual(actual, expected, msg)
