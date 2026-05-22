from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, you are at the polls index.")

def results(request):
    return HttpResponse("This is the page for displaying poll results!")
# Create your views here.
