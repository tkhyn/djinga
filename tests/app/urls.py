from django.conf.urls import patterns, url
from django.views.defaults import page_not_found

urlpatterns = patterns('',
    url('^not_found/$', page_not_found, name='notfound')
)
