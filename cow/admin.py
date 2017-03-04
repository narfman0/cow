from django.contrib import admin
from .models import MenuNode, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'last_updated')
    search_fields = ('id', 'name')
admin.site.register(Page, PageAdmin)


class MenuNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'page', 'enabled')
    search_fields = ('id', 'title', 'page', 'enabled')
admin.site.register(MenuNode, MenuNodeAdmin)
