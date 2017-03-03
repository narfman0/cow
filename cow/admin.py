from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'last_updated')
    search_fields = ('id', 'name')
admin.site.register(Page, PageAdmin)
