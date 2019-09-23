from django.conf.urls import url, include
from django.urls import path, re_path

from . import views

app_name='usermanagement'

urlpatterns = [
    re_path(r'^api/bond-categories/$', views.APIIndex.as_view(), name="bond_categories"),
]