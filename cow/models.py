# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from sorl.thumbnail import ImageField
from tinymce.models import HTMLField


@python_2_unicode_compatible
class Page(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    content = HTMLField(blank=True, null=True)
    plugins = models.ManyToManyField('Plugin', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Page: ' + str(self.name)


@python_2_unicode_compatible
class MenuNode(models.Model):
    title = models.CharField(max_length=200)
    page = models.ForeignKey(Page, null=True, blank=True)
    children = models.ManyToManyField('self', blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return 'MenuNode: ' + str(self.title)


@python_2_unicode_compatible
class Plugin(models.Model):
    position = models.PositiveSmallIntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return 'Plugin: ' + str(self.content_type) + " " + str(self.object_id)


@python_2_unicode_compatible
class TextPlugin(models.Model):
    content = HTMLField()

    def __str__(self):
        return 'TextPlugin: ' + str(self.content)[:40] + "..."


@python_2_unicode_compatible
class AddressPlugin(models.Model):
    address = models.CharField(max_length=200)

    def __str__(self):
        return 'AddressPlugin: ' + str(self.address)


@python_2_unicode_compatible
class ImagePlugin(models.Model):
    image = ImageField(upload_to="images")

    def __str__(self):
        return 'ImagePlugin: ' + str(self.image)
