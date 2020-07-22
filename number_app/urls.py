from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('to_high', views.high),
    path('to_low', views.low),
    path('correct', views.correct),
    path('check', views.check),
    path('end', views.end),
    path('lose', views.lose),
]