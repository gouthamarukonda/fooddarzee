
from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def get_home_page(request):
	if request.method == 'GET':
		return render(request, 'index.html')

@csrf_exempt
def get_daily_menu():
	if request.method == 'GET':
		date = datetime.now().date().date
		month = datetime.now().date().month
		year = datetime.now().date().year
		string = year+"-"+month+"-"+date

		qry = "select * from menu where date = %s"
		resultset = pgExecQuery(qry, string)

		print(resultset)

	else:
		pass