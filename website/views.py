
from django.shortcuts import render

# Create your views here.

import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dbHandler import *

def get_home_page(request):
	if request.method == 'GET':
		return render(request, 'index.html')