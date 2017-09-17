from django.shortcuts import render

from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect



# Create your views here.

def nothing_here(request):
	return HttpResponse("Nothing Here!")
	
def housing(request):
	
	
	return render(request, 'housing.html')

