from django.conf import settings

from .base import TestCase
from .compat import context_processors_module


class ContextProcessorsTests(TestCase):

    options = {'context_processors': [
        '%s.static' % context_processors_module,
    ]}
    template = '{{ STATIC_URL }}'

    def test_static(self):
        self.assertRender(settings.STATIC_URL)
