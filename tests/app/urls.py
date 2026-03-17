from django.urls import path
from django.views.defaults import page_not_found

urlpatterns = [
    path('not_found/', page_not_found, name='notfound'),
]
