from rest_framework import serializers, viewsets
from .models import Page, Plugin, MenuNode


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


class MenuNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuNode
        fields = ('id', 'title', 'page', 'children', 'enabled')


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = MenuNode.objects.all()
    serializer_class = MenuNodeSerializer
