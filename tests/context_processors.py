from django.conf import settings

from .base import TestCase


class ContextProcessorsTests(TestCase):

    options = {'context_processors': [
        'django.template.context_processors.static',
    ]}
    template = '{{ STATIC_URL }}'

    def test_static(self):
        self.assertRender(settings.STATIC_URL)
