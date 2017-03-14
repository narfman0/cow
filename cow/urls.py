# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from . import views
from . import api


router = routers.DefaultRouter()
router.register(r'pages', api.PageViewSet)
router.register(r'menus', api.MenuViewSet)


urlpatterns = [
    url('^api/', include(router.urls)),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(
        regex="^page/$",
        view=views.PageListView.as_view(),
        name='page_list',
    ),
    url(
        regex="^page/create/$",
        view=csrf_exempt(views.PageCreateView.as_view()),
        name='page_create',
    ),
    url(
        regex="^page/(?P<pk>\d+)/$",
        view=views.PageDetailView.as_view(),
        name='page_detail',
    ),
    url(
        regex="^page/(?P<pk>\d+)/plugin/create/$",
        view=views.PluginCreateView.as_view(),
        name='plugin_create',
    ),
    url(
        regex="^plugin/delete/(?P<pk>\d+)/$",
        view=views.PluginDeleteView.as_view(),
        name='plugin_delete',
    ),
    url(
        regex="^plugin/text/(?P<pk>\d+)/$",
        view=views.TextPluginUpdateView.as_view(),
        name='text_plugin_edit',
    ),
    url(
        regex="^plugin/address/(?P<pk>\d+)/$",
        view=views.AddressPluginUpdateView.as_view(),
        name='address_plugin_edit',
    ),
    url(
        regex="^plugin/image/(?P<pk>\d+)/$",
        view=views.ImagePluginUpdateView.as_view(),
        name='image_plugin_edit',
    ),
]
