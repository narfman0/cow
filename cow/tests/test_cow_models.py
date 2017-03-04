#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cow
------------

Tests for `cow` models module.
"""
from datetime import timedelta
from uuid import uuid4

from django.test import TestCase
from django.utils import timezone

from cow import models


class TestCow(TestCase):
    def test_page_simple(self):
        # stupid test to touch code/models
        page = models.Page.objects.create(name='test1', content='2')
        page.delete()

    def test_menu_node_simple(self):
        page = models.Page.objects.create(name='test1', content='2')
        child = models.MenuNode.objects.create(title='title1', page=page)
        parent = models.MenuNode.objects.create(title='title1')
        parent.children.add(child)
        parent.save()
        self.assertTrue(len(parent.children.values()) > 0)
        parent.delete()
        child.delete()
        page.delete()
