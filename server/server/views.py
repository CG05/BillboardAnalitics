from django.shortcuts import render
from django.http import HttpResponse

def mainpage(request):
    return render(request, 'main.html')

def examplepage(request):
    return render(request, 'contentexample.html')