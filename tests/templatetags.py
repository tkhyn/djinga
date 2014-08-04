from .base import TestCase


class DjangoTemplateTagsTests(TestCase):

    def test_extends(self):
        self.template_file = 'extends/django.djhtml'
        self.assertRender(' \nThis is a minimal django template that extends '
                          'a jinja template.\n ')
