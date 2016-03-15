# -*- coding: utf-8 -*-
from django.conf.urls import url

from reservation import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order/$', views.order, name='order'),
    url(r'^order/(?P<order>\d+)/$', views.order, name='change_order'),
    url(r'^order/(?P<order>\d+)/archive/$', views.archive_order, name='archive_order'),
]
