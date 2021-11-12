from django import http
from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def DEV(request):
    return render(request,'dev.html')

def PLAY(request):
    return render(request,'play.html')



