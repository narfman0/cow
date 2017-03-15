#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cow
------------

Tests for `cow` models module.
"""
from django.test import TestCase

from cow import models


class TestCow(TestCase):
    def test_page_simple(self):
        # stupid test to touch code/models
        page = models.Page.objects.create(name='test1')
        page.delete()

    def test_menu_node_simple(self):
        # create a page and point at it with model
        page = models.Page.objects.create(name='test1')
        child = models.Menu.objects.create(title='title1', page=page)
        parent = models.Menu.objects.create(title='title1')
        parent.children.add(child)
        parent.save()
        self.assertTrue(parent.children.count() > 0)
        parent.delete()
        child.delete()
        page.delete()

    def test_plugins(self):
        # create a text plugin, apply to page, and retrieve
        text_plugin_content = 'yo'
        page = models.Page.objects.create(name='test1')
        text_plugin = models.TextPlugin.objects.create(content=text_plugin_content)
        plugin = models.Plugin.objects.create(content_object=text_plugin)
        page.plugins.add(plugin)
        self.assertTrue(page.plugins.count() > 0)
        self.assertEquals(page.plugins.first().content_object.content, text_plugin_content)
        text_plugin.delete()
        plugin.delete()
        page.delete()

