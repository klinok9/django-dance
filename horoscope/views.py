from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def leo(reuest):
    return HttpResponse("Знак зодиака лев")

def scorpio(request):
    return HttpResponse("знак зодиака скорпион")
