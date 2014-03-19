"""
Jinja2 environment container and functions, settings defaults and loader

(c) Thomas Khyn 2014
"""

import os
import jinja2

from django.template import loader
from django.conf import settings
from django.template.context import BaseContext
from django.template import Origin

# Jinja2 settings loader and defaults

JJ_EXTS = getattr(settings, 'JINJA2_JJ_EXTS', ('jjhtml', 'jjhtm'))
DJ_EXTS = getattr(settings, 'JINJA2_DJ_EXTS', ('html', 'htm',
                                               'djhtml', 'djhtm'))
TEMPLATE_EXTS = JJ_EXTS + DJ_EXTS
CONDITION = getattr(settings, 'JINJA2_CONDITION',
    lambda path: os.path.basename(path).split('.')[-1] in JJ_EXTS)

CSS_DIR = getattr(settings, 'JINJA2_STATIC_CSS', 'css')
JS_DIR = getattr(settings, 'JINJA2_STATIC_JS', 'js')

OPTIONS = getattr(settings, 'JINJA2_ENV_ARGS', {})
GLOBALS = getattr(settings, 'JINJA2_GLOBALS', {})
FILTERS = getattr(settings, 'JINJA2_FILTERS', {})
EXTENSIONS = getattr(settings, 'JINJA2_EXTENSIONS', {})
# optional parameter JINJA2_I18N_NEWSTYLE can be provided (boolean)


def ctxt_to_dict(ctxt):
    """
    Helper function to convert a django context into a dictionary
    """
    if isinstance(ctxt, BaseContext):
        ctxt_dict = {}
        for d in ctxt.dicts:
            ctxt_dict.update(d)
        return ctxt_dict
    return dict(ctxt)


class DjingaTemplate(jinja2.Template):
    """
    Adapter class for jinja2 templates
    """

    def render(self, context=None):
        if context == None: context = {}

        new_ctxt = ctxt_to_dict(context)

        if settings.TEMPLATE_DEBUG:
            # send django signal on template rendering if in debug mode
            from django.test import signals
            self.origin = Origin(self.filename)
            signals.template_rendered.send(sender=self,
                                           template=self,
                                           context=context)

        return super(DjingaTemplate, self).render(new_ctxt)


    def stream(self, context=None):
        if context == None: context = {}

        new_ctxt = ctxt_to_dict(context)

        if settings.TEMPLATE_DEBUG:
            # send django signal on template rendering if in debug mode
            from django.test import signals
            self.origin = Origin(self.filename)
            signals.template_rendered.send(sender=self,
                                           template=self,
                                           context=context)

        return super(DjingaTemplate, self).stream(new_ctxt)


class Environment(jinja2.Environment):
    """
    Jinja2 environment subclass
    """

    def __init__(self, *args, **kwargs):
        super(Environment, self).__init__(*args, **kwargs)

        # install i18n if USE_I18N is true
        if settings.USE_I18N:
            self.add_extension('jinja2.ext.i18n')
            from django.utils import translation
            self.install_gettext_translations(translation,
                newstyle=getattr(settings, 'JINJA2_I18N_NEWSTYLE', False))

        # template loader
        template_dirs = [x for ldr_str in settings.TEMPLATE_LOADERS\
            for x in loader.find_template_loader(ldr_str)\
            .get_template_sources('')]
        self.loader = jinja2.FileSystemLoader(template_dirs)

        # template class
        self.template_class = DjingaTemplate

        # add filters
        for k, f in FILTERS.iteritems():
            self.filters[k] = f

        # add globals
        for k, g in GLOBALS.iteritems():
            self.globals[k] = g

        # add djinga specific options
        self.use_jinja = CONDITION
        self.css_dir = CSS_DIR
        self.js_dir = JS_DIR


env = Environment(**dict(OPTIONS, **{
    'extensions':EXTENSIONS,
}))
