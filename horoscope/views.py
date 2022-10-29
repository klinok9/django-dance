from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
# def Aries(reuest):
#     return HttpResponse("Знак зодиака Aries")
#
#
# def Taurus(request):
#     return HttpResponse("знак зодиака Taurus")
#
#
# def Gemini(request):
#     return HttpResponse("знак зодиака Gemini")
#
#
# def Cancer(request):
#     return HttpResponse("знак зодиака Cancer")
#
#
# def Leo(request):
#     return HttpResponse("знак зодиака Leo")
#
#
# def Virgo(request):
#     return HttpResponse("знак зодиака Virgo")
#
#
# def Libra(request):
#     return HttpResponse("знак зодиака Libra")
#
#
# def Scorpio(request):
#     return HttpResponse("знак зодиака Libra")
#
#
# def Sagittarius(request):
#     return HttpResponse("знак зодиака Sagittarius")
#
#
# def Capricorn(request):
#     return HttpResponse("знак зодиака Capricorn")
#
#
# def Aquarius(request):
#     return HttpResponse("знак зодиака Aquarius")
#
# def Pisces(request):
#     return HttpResponse("знак зодиака Pisces")

# Динамический Url
# def info_about_sign (requst, sign_zodiak):
#     if sign_zodiak == 'leo':
#         return HttpResponse("знак зодиака leo")
#     elif sign_zodiak == 'Aries':
#         return HttpResponse("Знак зодиака Aries")
#     elif sign_zodiak == 'Taurus':
#         return HttpResponse("Знак зодиака Taurus")
#     else:
#         return HttpResponseNotFound(f'{sign_zodiak} - ne znak')


# Убираем if, elif. Создаем словарь

zodiac_dict = {
    'leo': "знак зодиака leo",
    'Aries': "Знак зодиака Aries",
    'Taurus': "Знак зодиака Taurus"
}


def info_about_sign(requst, sign_zodiak:str):
    description = zodiac_dict.get(sign_zodiak)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'{sign_zodiak} - ne znak')


def info_about_sign_numb(requst, sign_zodiak:int):
    zodiacs = list(zodiac_dict)
    if sign_zodiak > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный номер! - {sign_zodiak}')
    name_zodiac = zodiacs[sign_zodiak-1]
    return HttpResponseRedirect(f'/horoscope/{name_zodiac}') # если число = индекс словаря то перенеправление работает
