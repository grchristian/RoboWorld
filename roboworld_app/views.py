from django.shortcuts import render
import psychopg2


'''
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from . models import Reto
import psycopg2
'''

def inicio(request):
    return render(request, "roboworld_app/index.html")

def stats(request):
    return render(request, "roboworld_app/stats.html")

def juego_unity(request):
    return render(request, "roboworld_app/juego_unity/index_unity.html")

def iniciar_sesion(request):
    return render(request, "roboworld_app/iniciar_sesion.html")

def micuenta(request):
    nombre = "Rebeca"
    num_engranes = "43"
    min_jugados = "53"
    veces_jugadas = "5"
    return render(request, "roboworld_app/micuenta.html", {"nombre":nombre,"num_engranes":num_engranes,"min_jugados":min_jugados,"veces_jugadas":veces_jugadas}) 


'''
def login(request):
    return render(request, "roboworld_app/login.html")

def logged_out(request):
    return render(request, "roboworld_app/logged_out.html")


def score(request):
    return render(request, "roboworld_app/score.html")
'''
