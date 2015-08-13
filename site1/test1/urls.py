from django.conf.urls import patterns, url, include
from django.views.generic import ListView

from . import models

urlpatterns = patterns('',
    (r'^list/$', ListView.as_view(
        model=models.Scan,
    )),
)
