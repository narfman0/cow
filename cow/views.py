# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, UpdateView

from .forms import PluginCreateForm
from .models import AddressPlugin, ImagePlugin, Menu, Page, Plugin, TextPlugin
from . import plugin_map


class MenuCreateView(CreateView):
    model = Menu
    fields = ['title', 'page', 'children', 'root', 'enabled']
    success_url = reverse_lazy('page_list')


class MenuChildCreateView(CreateView):
    model = Menu
    fields = ['title', 'page', 'children', 'root', 'enabled']

    def form_valid(self, form):
        parent = Menu.objects.get(pk=int(self.kwargs['pk']))
        form.instance.save()
        parent.children.add(form.instance)
        return redirect('menu_detail', pk=form.instance.pk)


class MenuDetailView(DetailView):
    model = Menu


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('page_list')

    def delete(self, request, *args, **kwargs):
        menu = Menu.objects.get(pk=kwargs['pk'])
        for menu in menu.children.all():
            menu.delete()
        return super(MenuDeleteView, self).delete(self, request, args, kwargs)


class MenuUpdateView(UpdateView):
    fields = ['title', 'page', 'children', 'root', 'enabled']
    model = Menu

    def get_success_url(self):
        return reverse('menu_detail', kwargs={'pk': self.object.pk})


class PageListView(ListView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        context['menus'] = Menu.objects.filter(root=True)
        return context


class PageCreateView(CreateView):
    model = Page
    fields = ['name', ]
    success_url = reverse_lazy('page_list')


class PageUpdateView(UpdateView):
    template_name = 'cow/page_update.html'
    model = Page
    fields = ['name', ]


class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('page_list')

    def delete(self, request, *args, **kwargs):
        page = Page.objects.get(pk=kwargs['pk'])
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
        return redirect('page_update', pk=page_id)


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
    fields = ['content', ]
    model = TextPlugin

    def get_success_url(self):
        return reverse('text_plugin_edit', kwargs={'pk': self.object.pk})
