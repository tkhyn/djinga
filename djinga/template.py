import jinja2

from django.conf import settings
from django.template.context import BaseContext
from django.template import Origin


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
        if context == None:
            context = {}

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
        if context == None:
            context = {}

        new_ctxt = ctxt_to_dict(context)

        if settings.TEMPLATE_DEBUG:
            # send django signal on template rendering if in debug mode
            from django.test import signals
            self.origin = Origin(self.filename)
            signals.template_rendered.send(sender=self,
                                           template=self,
                                           context=context)

        return super(DjingaTemplate, self).stream(new_ctxt)
