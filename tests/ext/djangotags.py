import mock

from django.template.defaulttags import CsrfTokenNode

from jinja2 import Markup

from tests._base import ExtTestCase


class DjangoTagsTests(ExtTestCase):

    options = {
        'context_processors': [
            'django.template.context_processors.request',
        ],
    }
    extensions = ('djinga.ext.django',)

    def test_django_tag(self):
        # using django specific template tags, without spaces nor linebreaks
        self.template = \
            '{% django %}' \
            '{% load i18n %}' \
            '{% blocktrans %}To be translated{% endblocktrans %}' \
            '{% enddjango %}'
        self.assertRender('To be translated')

    def test_django_tag_file(self):
        # using django specific template tags, without spaces nor linebreaks
        self.template_file = 'djangotag/jinja.jjhtml'
        self.assertRender('\n\nTo be translated\n')


class CsrfTest(ExtTestCase):

    extensions = ('djinga.ext.csrf_token',)
    options = {
        'context_processors': [
            'django.template.context_processors.csrf',
        ],
    }
    template = '{% csrf_token %}'

    @mock.patch('django.template.context_processors.get_token')
    def test_csrf_token(self, get_token):
        self.template = '{% csrf_token %}'
        get_token.return_value = csrf_token = 'CSRFTOKEN'
        self.assertRender(
            Markup(CsrfTokenNode().render({'csrf_token': csrf_token})),
            {'csrf_token': csrf_token})
