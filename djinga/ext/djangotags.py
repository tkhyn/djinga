"""
Extensions to use Django template language within Jinja2 templates
"""

from django import template as dj_template
from django.core.exceptions import ImproperlyConfigured

from jinja2 import nodes, contextfunction
from jinja2.ext import Extension


class DjangoTag(Extension):
    # from https://github.com/coffin/coffin/pull/12/files?short_path=88b99bb&unchanged=collapsed

    tags = set(['django'])

    def preprocess(self, source, name, filename=None):
        source = source.replace('{% django %}', '{% django %}{% raw %}')
        source = source.replace('{% enddjango %}',
                                '{% endraw %}{% enddjango %}')
        return source

    def parse(self, parser):
        lineno = parser.stream.next().lineno
        while not parser.stream.next().test('block_end'):
            pass
        body = nodes.Const(parser.stream.next().value)
        while not parser.stream.current.test('block_end'):
            parser.stream.next()
        return nodes.Output([
            self.call_method('_django', args=[body], kwargs=[]),
        ]).set_lineno(lineno=lineno)

    @contextfunction
    def _django(self, context, html):
        request = context.get('request', None)
        if not request:
            raise ImproperlyConfigured(
                'You need to enable the django.core.context_processors.request '
                'context processor to use the {% django %} tag in Jinja2 '
                'templates.')
        context = dj_template.RequestContext(request, context)
        return dj_template.Template(html).render(context)
