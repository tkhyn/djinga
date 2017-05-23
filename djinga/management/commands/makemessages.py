"""
Adapted from coffin, https://github.com/coffin/coffin
(c) Coffin contributors
3-clause BSD License

Jinja2's i18n functionality is not exactly the same as Django's.
In particular, the tags names and their syntax are different:

  1. The Django ``trans`` tag is replaced by a _() global.
  2. The Django ``blocktrans`` tag is called ``trans``.

(1) isn't an issue, since the whole ``makemessages`` process is based on
converting the template tags to ``_()`` calls. However, (2) means that
those Jinja2 ``trans`` tags will not be picked up my Django's
``makemessage`` command.

There aren't any nice solutions here. While Jinja2's i18n extension does
come with extraction capabilities built in, the code behind ``makemessages``
unfortunately isn't extensible, so we can:

  * Duplicate the command + code behind it.
  * Offer a separate command for Jinja2 extraction.
  * Try to get Django to offer hooks into makemessages().
  * Monkey-patch.

We are currently doing that last thing. It turns out there we are lucky
for once: It's simply a matter of extending two regular expressions.
Credit for the approach goes to:
http://stackoverflow.com/questions/2090717/
getting-translation-strings-for-jinja2-templates-integrated-with-django-1-x
"""

import re
from django.core.management.commands import makemessages
from django.template.base import BLOCK_TAG_START, BLOCK_TAG_END
from django.template import engines

try:
    from django.utils.translation import template
except ImportError:
    from django.utils.translation import trans_real as template


strip_whitespace_right = re.compile(
    r"(%s-?\s*(trans|pluralize).*?-%s)\s+" % \
    (BLOCK_TAG_START, BLOCK_TAG_END), re.U)
strip_whitespace_left = re.compile(
   r"\s+(%s-\s*(endtrans|pluralize).*?-?%s)" % \
   (BLOCK_TAG_START, BLOCK_TAG_END), re.U)


def strip_whitespaces(src):
    src = strip_whitespace_left.sub(r'\1', src)
    src = strip_whitespace_right.sub(r'\1', src)
    return src


class Command(makemessages.Command):

    def handle(self, *args, **options):

        if not options['extensions']:
            options['extensions'] = list(engines['djinga'].env.template_exts)

        old_endblock_re = template.endblock_re
        old_block_re = template.block_re
        old_templatize = template.templatize
        # Extend the regular expressions that are used to detect
        # translation blocks with an "OR jinja-syntax" clause.
        template.endblock_re = re.compile(
            template.endblock_re.pattern + '|' + \
            r"""^-?\s*endtrans\s*-?$""")
        template.block_re = re.compile(
            template.block_re.pattern + '|' + \
            r"""^-?\s*trans(?:\s+(?!'|")(?=.*?=.*?)|-?$)""")
        template.plural_re = re.compile(
            template.plural_re.pattern + '|' + \
            r"""^-?\s*pluralize(?:\s+.+|-?$)""")

        def my_templatize(src, origin=None):
            new_src = strip_whitespaces(src)
            return old_templatize(new_src, origin)

        template.templatize = my_templatize

        try:
            super(Command, self).handle(**options)
        finally:
            template.endblock_re = old_endblock_re
            template.block_re = old_block_re
            template.templatize = old_templatize
