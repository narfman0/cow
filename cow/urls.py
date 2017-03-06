# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
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
]
