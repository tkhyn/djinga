from django.conf.urls import url
from django.views.defaults import page_not_found

try:
    from django.conf.urls import patterns
except ImportError:
    patterns = None


urlpatterns = [
    url('^not_found/$', page_not_found, name='notfound')
]


if patterns is not None:
    urlpatterns = patterns('', *urlpatterns)
