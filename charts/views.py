from django.shortcuts import render
from django.http import HttpResponse
from charts.models import SalesReport
from chartit import DataPool, Chart
from django.db.models import Avg, Sum, Count, Min, Max

def sales(request):
	sales= DataPool(
		series=
		[
		{'options': {'source':SalesReport},
		'terms':[{'month':'month',
		'sales':'sales'}]
		}
		])
	def monthname(month_num):
		names={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',
				7:'July',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
		return names[month_num]

	cht=Chart(
		datasource=sales,
		series_options=
		[{'options':{
			'type': 'column',
			'stacking': False },
			'terms':{
			'month':['sales']
			}}],
		chart_options=
		{"title":{"text": "Sales Amounts over months"},
			"xAxis":{"title":{"text":"Sales Total"}},
			"yAxis":{"title":{"text":"Month Number"}},
			"legend":{"enabled":True},
			"credits":{"enabled":True}},
		x_sortf_mapf_mts=(None,monthname,False)
			)
	cht2=Chart(
		datasource=sales,
		series_options=
		[{'options':{
			'type': 'pie',
             'plotBorderWidth': 1,
              'zoomType': 'xy',              
              'legend':{'enabled': True,}},
			'terms':{'month':['sales']}
			}],
		chart_options=
		{"title":{"text": "Sales Amounts over months"},
			"xAxis":{"title":{"text":"Sales Total"}},
			"yAxis":{"title":{"text":"Month Number"}},
			"legend":{"enabled":True},
			"credits":{"enabled":True}},
		x_sortf_mapf_mts=(None,monthname,False)
			)
	return render(request,'sales.html',{'chart_list':[cht,cht2]})
# Create your views here.
