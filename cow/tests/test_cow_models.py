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
    def setUp(self):
        self.pages = []
        for i in range(9):
            page = models.Page.objects.create(name='test1', content=str(i))
            self.pages.append(page)
            page.created -= timedelta(days=i)
            page.save()

    def test_generate_simple(self):
        # stupid test to touch code/models
        extra = models.Page.objects.create(name='test1', content='2')
        extra.delete()

    def tearDown(self):
        for page in self.pages:
            page.delete()
