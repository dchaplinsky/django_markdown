""" Define preview URL. """

from django.urls import path
from django.conf.urls import include

from .views import preview

urlpatterns = [
    path('preview/', preview, name='django_markdown_preview')
]
