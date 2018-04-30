
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

		qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		resultset = pgExecQuery(qry, [string])
		bf_veg = resultset[0].name

		# qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		# resultset = pgExecQuery(qry, [string])
		# lunch_veg = resultset[0].name

		# qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		# resultset = pgExecQuery(qry, [string])
		# snacks_veg = resultset[0].name

		# qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		# resultset = pgExecQuery(qry, [string])
		# dinner_veg = resultset[0].name

		# qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		# resultset = pgExecQuery(qry, [string])
		# bf_veg = resultset[0].name

		# qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		# resultset = pgExecQuery(qry, [string])
		# bf_veg = resultset[0].name

		# qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		# resultset = pgExecQuery(qry, [string])
		# bf_veg = resultset[0].name

		# qry = "select dish.name from menu full outer join dish on dish.id = menu.dish_id where date = %s and meal_time = 'Breakfast' and menu.type = 'Vegetarian'"
		# resultset = pgExecQuery(qry, [string])
		# bf_veg = resultset[0].name





		return render(request, 'index.html', {'bf_veg' : bf_veg})