from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_here':"From views.py..."}
    return render(request, 'showstations/index.html', context=my_dict)