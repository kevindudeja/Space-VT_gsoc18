from django.shortcuts import render
from django.views.generic import TemplateView
from pygal.style import DarkStyle

from .charts import decLineChart, novLineChart

# Create your views here.
from .models import dst_2013 as dst

def index(request):
	context={}
	return render(
		request,
		'index.html',
		context,
	)

def dec_2013(request):
	template_name = 'dec_2013.html'
	days = dst.objects.all()[0]
	context = {}
	# Instantiate our chart. We'll keep the size/style/etc.
	# config here in the view instead of `charts.py`.
	cht_dst = decLineChart(height=300,width=1100,explicit_size=True,style=DarkStyle)
	# Call the `.generate()` method on our chart object
	# and pass it to template context.
	context['cht_dst'] = cht_dst.generate()
	context['d1'] = days.d1
	context['d2'] = days.d2
	context['d3'] = days.d3
	context['d4'] = days.d4
	context['d5'] = days.d5
	context['d6'] = days.d6
	context['d7'] = days.d7
	context['d8'] = days.d8
	context['d9'] = days.d9
	context['d10'] = days.d10
	return render(
		request,
		'dec_2013.html',
		context,
	)
def nov_2013(request):
	template_name = 'nov_2013.html'
	days = dst.objects.all()[1]
	context = {}
	# Instantiate our chart. We'll keep the size/style/etc.
	# config here in the view instead of `charts.py`.
	cht_nov = novLineChart(height=300,width=1100,explicit_size=True,style=DarkStyle)
	# Call the `.generate()` method on our chart object
	# and pass it to template context.
	context['cht_nov'] = cht_nov.generate()
	context['d1'] = days.d1
	context['d2'] = days.d2
	context['d3'] = days.d3
	context['d4'] = days.d4
	context['d5'] = days.d5
	context['d6'] = days.d6
	context['d7'] = days.d7
	context['d8'] = days.d8
	context['d9'] = days.d9
	context['d10'] = days.d10
	return render(
		request,
		'nov_2013.html',
		context,
	)
"""
def index(request):
	num_days = dec.objects.all()[0]
	days = dec.objects.all()[0]
	
	return render(
		request,
		'index.html',
		context = {'num_days':num_days,'days':days}
	)
"""
