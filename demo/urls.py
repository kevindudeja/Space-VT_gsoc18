from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('dec_2013', views.dec_2013, name='dec_2013'),
	path('nov_2013', views.nov_2013, name='nov_2013'),
]