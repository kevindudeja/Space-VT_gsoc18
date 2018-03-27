import pygal

from .models import dst_2013

class decLineChart():
	def __init__(self, **kwargs):
		self.chart = pygal.Line(**kwargs)
		self.chart.title = 'DST INDEX OF DECEMBER 2013'
		
	def get_data(self):
		dataInt = []
		d = dst_2013.objects.get(pk=1)
		comma = ","
		seq = (d.d1,d.d2,d.d3,d.d4,d.d5,d.d6,d.d7,d.d8,d.d9,d.d10,d.d11,d.d12,d.d13,d.d14,d.d15,d.d16,d.d17,d.d18,d.d19,d.d20,d.d21,d.d22,d.d23,d.d24,d.d25,d.d26,d.d27,d.d28,d.d29,d.d30,d.d31)
		days = comma.join(seq)
		days = days.replace("    ",",")
		days = days.replace("   ",",")
		days = days.replace("  ",",")
		days = days.replace(" ",",")
		data = days.split(",")
		for i in data:
			dataInt.append(int(i))
		return dataInt
	
	def generate(self):
		chart_data = self.get_data()
		self.chart.add('December_2013',chart_data)
		return self.chart.render(is_unicode=True)

class novLineChart():
	def __init__(self, **kwargs):
		self.chart = pygal.Line(**kwargs)
		self.chart.title = 'DST INDEX OF NOVEMBER 2013'
		
	def get_data(self):
		dataInt = []
		d = dst_2013.objects.get(pk=2)
		comma = ","
		seq = (d.d1,d.d2,d.d3,d.d4,d.d5,d.d6,d.d7,d.d8,d.d9,d.d10,d.d11,d.d12,d.d13,d.d14,d.d15,d.d16,d.d17,d.d18,d.d19,d.d20,d.d21,d.d22,d.d23,d.d24,d.d25,d.d26,d.d27,d.d28,d.d29,d.d30)
		days = comma.join(seq)
		days = days.replace("    ",",")
		days = days.replace("   ",",")
		days = days.replace("  ",",")
		days = days.replace(" ",",")
		data = days.split(",")
		for i in data:
			dataInt.append(int(i))
		return dataInt
	
	def generate(self):
		chart_data = self.get_data()
		self.chart.add('November_2013',chart_data)
		return self.chart.render(is_unicode=True)
		
			