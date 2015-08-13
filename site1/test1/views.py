from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from . import models


class ScanCreate(CreateView):
    model = models.Scan
    fields = ['name', 'description','attributes']
