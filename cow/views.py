# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView

from .forms import PluginCreateForm, TextPluginForm
from .models import AddressPlugin, ImagePlugin, Page, Plugin, TextPlugin
from . import plugin_map


class PageListView(ListView):
    model = Page


class PageCreateView(CreateView):
    model = Page
    fields = ['name', ]
    success_url = reverse_lazy('page_list')


class PageDetailView(DetailView):
    model = Page


class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('page_list')

    def delete(self, request, *args, **kwargs):
        page = Page.objects.get(pk=kwargs['pk'])
        import pdb; pdb.set_trace()
        for page_plugin in page.plugins.all():
            page_plugin.content_object.delete()
            page_plugin.delete()
        return super(PageDeleteView, self).delete(self, request, args, kwargs)


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


class PluginDeleteView(DeleteView):
    model = Plugin
    success_url = reverse_lazy('page_list')

    def delete(self, request, *args, **kwargs):
        plugin = Plugin.objects.get(pk=kwargs['pk'])
        plugin.content_object.delete()
        return super(PluginDeleteView, self).delete(self, request, args, kwargs)


class AddressPluginUpdateView(UpdateView):
    fields = ['address', ]
    model = AddressPlugin

    def get_success_url(self):
        return reverse('address_plugin_edit', kwargs={'pk': self.object.pk})


class ImagePluginUpdateView(UpdateView):
    fields = ['image', ]
    model = ImagePlugin

    def get_success_url(self):
        return reverse('image_plugin_edit', kwargs={'pk': self.object.pk})


class TextPluginUpdateView(UpdateView):
    form_class = TextPluginForm
    model = TextPlugin

    def get_success_url(self):
        return reverse('text_plugin_edit', kwargs={'pk': self.object.pk})
