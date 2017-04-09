from django.conf import settings
from rest_framework import serializers, viewsets
from .models import Menu, Page, Plugin


# lolworthily high, also the max :)
MENU_DEPTH = getattr(settings, 'COW_API_MENU_DEPTH', 10)


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'name', 'plugins')

    def to_representation(self, instance):
        data = super(PageSerializer, self).to_representation(instance)
        plugins_api = []
        for plugin_id in data['plugins']:
            plugin = Plugin.objects.get(pk=int(plugin_id))
            plugins_api.append(plugin.content_object.api_serialize())
        data['plugins'] = plugins_api
        return data


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        depth = MENU_DEPTH
        model = Menu
        fields = ('id', 'title', 'enabled', 'root', 'children')


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(root=True)
    serializer_class = MenuSerializer
