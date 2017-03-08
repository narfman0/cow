# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView

from .forms import PluginCreateForm
from .models import AddressPlugin, ImagePlugin, Page, Plugin, TextPlugin
from . import plugin_map


class PageListView(ListView):
    model = Page


class PageCreateView(CreateView):
    model = Page
    fields = ['name',]
    success_url = reverse_lazy('page_list')


class PageDetailView(DetailView):
    model = Page


class PluginCreateView(FormView):
    template_name = 'cow/plugin_create.html'
    form_class = PluginCreateForm

    def form_valid(self, form):
        plugin_class = plugin_map[form.cleaned_data['plugin_type']]
        plugin_instance = plugin_class.objects.create()
        plugin = Plugin.objects.create(content_object=plugin_instance)
        page_id = int(filter(str.isdigit, str(self.request.path)))
        page = Page.objects.get(pk=page_id)
        page.plugins.add(plugin)
        return redirect('page_detail', pk=page_id)


class AddressPluginUpdateView(UpdateView):
    fields = ['address',]
    model = AddressPlugin

    def get_success_url(self):
        return reverse('address_plugin_edit', kwargs={'pk': self.object.pk})



class ImagePluginUpdateView(UpdateView):
    fields = ['image',]
    model = ImagePlugin

    def get_success_url(self):
        return reverse('image_plugin_edit', kwargs={'pk': self.object.pk})


class TextPluginUpdateView(UpdateView):
    fields = ['content',]
    model = TextPlugin

    def get_success_url(self):
        return reverse('text_plugin_edit', kwargs={'pk': self.object.pk})
