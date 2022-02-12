from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Hello!')

def ahula(request):
    return HttpResponse('Hello, Andrii!')

def david(request):
    return HttpResponse('Hello, David!')