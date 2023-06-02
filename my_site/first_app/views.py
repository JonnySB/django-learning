from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def simple_view(response):
    return HttpResponse('SIMPLE VIEW')