from django.urls import path

from . import views


urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('proceso',views.proceso, name = 'proceso'),
    path('datos',views.datos, name = 'datos'),
    path('stats/', views.stats, name="stats"),
    path('micuenta/', views.micuenta, name="micuenta"),
    path('juego_unity/', views.juego_unity, name="juego_unity"),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
    path('buscaJugadorBody', views.buscaJugadorBody, name='buscaJugadorBody'),
    path('ejemploSQL', views.ejemploSQL, name='ejemploSQL'),
    path('score',views.score, name = 'score'),
    path('grafica',views.grafica, name = 'grafica'),

    path('index2',views.index2, name = 'index2')
]



