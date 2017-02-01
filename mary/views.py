from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
import mary
import templates

def get(request):
    return HttpResponse("hello world")

def index(request):
      render(request,'mary/index.html',context=None)

