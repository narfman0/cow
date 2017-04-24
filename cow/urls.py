# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views
from . import api


router = routers.DefaultRouter()
router.register(r'pages', api.PageViewSet)
router.register(r'menus', api.MenuViewSet)


urlpatterns = [
    url('^accounts/login/$', auth_views.login, {'template_name': 'admin/login.html'}, name='cow_login'),
    url('^api/', include(router.urls)),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(
        regex="^menu/create/$",
        view=login_required(views.MenuCreateView.as_view()),
        name='menu_create',
    ),
    url(
        regex="^menu/(?P<pk>\d+)/create/$",
        view=login_required(views.MenuChildCreateView.as_view()),
        name='menu_child_create',
    ),
    url(
        regex="^menu/delete/(?P<pk>\d+)/$",
        view=login_required(views.MenuDeleteView.as_view()),
        name='menu_delete',
    ),
    url(
        regex="^menu/update/(?P<pk>\d+)/$",
        view=login_required(views.MenuUpdateView.as_view()),
        name='menu_update',
    ),
    url(
        regex="^menu/(?P<pk>\d+)/$",
        view=login_required(views.MenuDetailView.as_view()),
        name='menu_detail',
    ),
    url(
        regex="^$",
        view=login_required(views.PageListView.as_view()),
        name='page_list',
    ),
    url(
        regex="^page/create/$",
        view=login_required(views.PageCreateView.as_view()),
        name='page_create',
    ),
    url(
        regex="^page/delete/(?P<pk>\d+)/$",
        view=login_required(views.PageDeleteView.as_view()),
        name='page_delete',
    ),
    url(
        regex="^page/(?P<pk>\d+)/$",
        view=login_required(views.PageUpdateView.as_view()),
        name='page_update',
    ),
    url(
        regex="^page/(?P<pk>\d+)/plugin/create/$",
        view=login_required(views.PluginCreateView.as_view()),
        name='plugin_create',
    ),
    url(
        regex="^plugin/delete/(?P<pk>\d+)/$",
        view=login_required(views.PluginDeleteView.as_view()),
        name='plugin_delete',
    ),
    url(
        regex="^plugin/text/(?P<pk>\d+)/$",
        view=login_required(views.TextPluginUpdateView.as_view()),
        name='text_plugin_edit',
    ),
    url(
        regex="^plugin/address/(?P<pk>\d+)/$",
        view=login_required(views.AddressPluginUpdateView.as_view()),
        name='address_plugin_edit',
    ),
    url(
        regex="^plugin/image/(?P<pk>\d+)/$",
        view=login_required(views.ImagePluginUpdateView.as_view()),
        name='image_plugin_edit',
    ),
]
