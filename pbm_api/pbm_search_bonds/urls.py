from django.conf.urls import url, include
from django.urls import path, re_path

from . import views

app_name='pbm_search_bonds'

urlpatterns = [
    re_path(r'^bond-search/$', views.BondsSearchAPIView.as_view(), name="bond_search"),
    # re_path(r'^api/draw-dates/(?P<category>[0-9]+)?$', views.BondDrawDatesAPIIndex.as_view(), name="bond_draw_dates"),
]