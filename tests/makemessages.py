import os
import shutil

from django.core.management import call_command

from .base import TestCase


class MakemessagesTests(TestCase):

    def setUp(self):
        self.locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
        os.mkdir(self.locale_dir)

    def tearDown(self):
        shutil.rmtree(self.locale_dir)

    def test_make_messages(self):
        call_command('makemessages', locale=('fr',))

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
