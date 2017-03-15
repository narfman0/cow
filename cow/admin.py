from django.contrib import admin
from .models import AddressPlugin, ImagePlugin, Menu, Page, Plugin, TextPlugin


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'last_updated')
    search_fields = ('id', 'name')
admin.site.register(Page, PageAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'page', 'enabled', 'root')
    search_fields = ('id', 'title', 'page', 'enabled', 'root')
admin.site.register(Menu, MenuAdmin)


class PluginAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'content_object')
    search_fields = ('id', 'position', 'content_object')
admin.site.register(Plugin, PluginAdmin)


class TextPluginAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
admin.site.register(TextPlugin, TextPluginAdmin)


class AddressPluginAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
    search_fields = ('id', 'address')
admin.site.register(AddressPlugin, AddressPluginAdmin)

admin.site.register(ImagePlugin)
