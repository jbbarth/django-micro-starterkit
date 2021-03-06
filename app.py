import os

import django_micro as micro
from django_micro import configure, route, run, template
from django.conf.urls import url
from django.shortcuts import render
from django.views import static


DEBUG = bool(os.getenv("DEBUG"))
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django_extensions',
]
TEMPLATE_DIRS = ['templates']
CONTEXT_PROCESSORS = ['django.template.context_processors.request']
TEMPLATES = [
    {
        'BACKEND': 'djangomako.backends.MakoBackend',
        'NAME': 'mako',
        'DIRS': TEMPLATE_DIRS,
    },
]
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'
ALLOWED_HOSTS = ['*']
configure(locals())


# serve static files even in production
micro.urlpatterns += [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': STATIC_ROOT}),
]


# GET /
@route(r'^$', name='index')
def index(request):
    return render(request, 'index.html', {})


# GET /about
@route(r'^about$', name='about')
def about(request):
    return render(request, 'about.html', {})


# A useful "|lookup" filter for dynamically retrieve dict values
@template.filter
def lookup(value, arg):
    if isinstance(value, dict):
        return value.get(arg)


# run the app!
application = run()
