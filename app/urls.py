from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from . import views

app_name = 'app'

urlpatterns = [
	path('', views.index, name='index'),
	path('etf-agg-data', views.etf_agg_data, name='etfAggData'),
]