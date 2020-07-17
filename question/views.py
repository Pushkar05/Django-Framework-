from django.http import HttpResponse
from django.shortcuts import render

#/question ->
#uniform Resource Locator (Address)
def index(request):
    return HttpResponse('Hello world')


def new(request):
    return HttpResponse('New')


# Create your views here.
