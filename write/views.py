from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def post(request):
    return HttpResponse("I posted my first Django app as a student of Semicolon ")


def like(request):
    return HttpResponse("I liked his post")


def message(request):
    return render(request,'message.html')
