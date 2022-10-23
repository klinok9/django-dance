from django.urls import path
from . import views  #from . импорт из этой папки (horoscope)

urlpatterns = [
    path('Aries/', views.Aries),  # 'horoscope/leo', представление которое в файлике views
    path('Taurus/', views.Taurus),
    path('Gemini/', views.Gemini),
    path('Cancer/', views.Cancer),
    path('Leo/', views.Leo),
    path('Virgo/', views.Virgo),
    path('Libra/', views.Libra),
    path('Scorpio/', views.Scorpio),
    path('Sagittarius/', views.Sagittarius),
    path('Capricorn/', views.Capricorn),
    path('Aquarius/', views.Aquarius),
    path('Pisces/', views.Pisces),

]
