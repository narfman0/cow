# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from . import register


@python_2_unicode_compatible
class Page(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    plugins = models.ManyToManyField('Plugin', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Page: ' + str(self.name)

    def get_absolute_url(self):
        return reverse('page_update', args=[self.id])


@python_2_unicode_compatible
class Menu(models.Model):
    title = models.CharField(max_length=200)
    page = models.ForeignKey(Page, null=True, blank=True)
    children = models.ManyToManyField('self', blank=True, symmetrical=False)
    enabled = models.BooleanField(default=True)
    root = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Menu: ' + str(self.title)


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
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'TextPlugin: ' + str(self.content)[:40] + "..."

    def api_serialize(self):
        return {
            'type': 'text',
            'content': self.content,
        }

    def get_absolute_url(self):
        return reverse('text_plugin_edit', args=[self.id])
register(TextPlugin, 'Text')


@python_2_unicode_compatible
class AddressPlugin(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return 'AddressPlugin: ' + str(self.address)

    def api_serialize(self):
        return {
            'type': 'address',
            'content': self.address,
        }

    def get_absolute_url(self):
        return reverse('address_plugin_edit', args=[self.id])
register(AddressPlugin, 'Address')


@python_2_unicode_compatible
class ImagePlugin(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return 'ImagePlugin: ' + str(self.image)

    def api_serialize(self):
        return {
            'type': 'image',
            'content': self.image.url,
        }

    def get_absolute_url(self):
        return reverse('image_plugin_edit', args=[self.id])
register(ImagePlugin, 'Image')
