import os
import shutil

import django
from django.core.management import call_command

from .base import TestCase


class MakemessagesTests(TestCase):

    def setUp(self):
        self.locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
        try:
            os.mkdir(self.locale_dir)
        except OSError:
            pass

    def tearDown(self):
        shutil.rmtree(self.locale_dir)

    def test_make_messages(self):
        loc = 'fr'
        if django.VERSION >= (1, 6):
            loc = [loc]
        call_command('makemessages', locale=loc)

        po_file = open(os.path.join(self.locale_dir, 'fr',
                                    'LC_MESSAGES', 'django.po'), 'r')
        po_ctnt = po_file.read()
        po_file.close()

        self.assertTrue('msgid "To be translated"' in po_ctnt)
        self.assertTrue('msgid "Between trans/endtrans"' in po_ctnt)
        self.assertTrue('msgid "One translated string"' in po_ctnt)
        self.assertTrue('msgid_plural "%(n)s translated strings"' in po_ctnt)
        self.assertTrue('msgid "Between braces and parenthesis"' in po_ctnt)

        self.assertEqual(po_ctnt.count('msgid'), 6)
