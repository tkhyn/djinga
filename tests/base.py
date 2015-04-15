from django import test
from django.template.loader import get_template
from django.template import Context, engines


# nose should not look for tests in this module
__test__ = False
__unittest = True


class TestCase(test.TestCase):

    extensions = ()
    template = ''
    template_file = ''

    def _pre_setup(self):
        super(TestCase, self)._pre_setup()
        self.old_options = engines.templates['djinga']['OPTIONS'].copy()
        self.setEnvironment(extensions=self.extensions)

    def setEnvironment(self, **kwargs):
        try:
            del engines._engines['djinga']
        except KeyError:
            pass
        engines.templates['djinga']['OPTIONS'] = kwargs
        engines['djinga']  # this reinitializes the djinga backend

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
