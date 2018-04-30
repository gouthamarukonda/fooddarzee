
from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dbHandler import *


def get_home_page(request):
	if request.method == 'GET':

		date = datetime.now().date().day
		month = datetime.now().date().month
		year = datetime.now().date().year
		string = str(year)+"-"+str(month)+"-"+str(date)

		qry = "select * from menu where date = %s and meal_time = %s"
		resultset = pgExecQuery(qry, [string, "Breakfast"])

		dish_id = resultset[0].dish_id


		return render(request, 'index.html', {'menu' : dish_id})