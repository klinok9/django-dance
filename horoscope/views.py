from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Aries(reuest):
    return HttpResponse("Знак зодиака Aries")


def Taurus(request):
    return HttpResponse("знак зодиака Taurus")


def Gemini(request):
    return HttpResponse("знак зодиака Gemini")


def Cancer(request):
    return HttpResponse("знак зодиака Cancer")


def Leo(request):
    return HttpResponse("знак зодиака Leo")


def Virgo(request):
    return HttpResponse("знак зодиака Virgo")


def Libra(request):
    return HttpResponse("знак зодиака Libra")


def Scorpio(request):
    return HttpResponse("знак зодиака Libra")


def Sagittarius(request):
    return HttpResponse("знак зодиака Sagittarius")


def Capricorn(request):
    return HttpResponse("знак зодиака Capricorn")


def Aquarius(request):
    return HttpResponse("знак зодиака Aquarius")

def Pisces(request):
    return HttpResponse("знак зодиака Pisces")
