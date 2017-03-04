# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from tinymce.models import HTMLField


@python_2_unicode_compatible
class Page(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    content = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Page: ' + str(self.name)


@python_2_unicode_compatible
class MenuNode(models.Model):
    title = models.CharField(max_length=200)
    page = models.ForeignKey(Page, null=True, blank=True)
    children = models.ManyToManyField('self')
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return 'MenuNode: ' + str(self.title)
