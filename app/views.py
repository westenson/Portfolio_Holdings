from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .analysis import *

def index(request):
    template_name = 'app/index.html'
    return render(request, template_name)

@api_view(['GET'])
def etf_agg_data(request):

	etf_dict = {
		"VWO": 1,
		"SPY": 1
	}

	if request.method == 'GET':
		return Response(get_overall_holdings(etf_dict)["Amount Owned"].to_dict())
