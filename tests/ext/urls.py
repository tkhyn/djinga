from tests.base import ExtTestCase


class StaticTests(ExtTestCase):

    extensions = ('djinga.ext.url',)

    def test_reverse_url(self):
        self.template = "{% url 'notfound' %}"
        self.assertRender('/not_found/')
