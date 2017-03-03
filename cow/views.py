# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .models import Page


class PageListView(ListView):
    model = Page


class PageCreateView(CreateView):
    model = Page
    fields = ['name', 'content']
    success_url = reverse_lazy('page_list')


class PageDetailView(DetailView):
    model = Page
