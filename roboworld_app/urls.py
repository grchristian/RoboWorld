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
   
]


'''
    path('login/', views.login, name="login"),
    path('logged_out/', views.logged_out, name="logged_out"),
    path('score/', views.score, name="score"),
'''
 '''
    path('score',views.Level, name = 'level'),
    path('score',views.Engranes, name = 'engranes'),
    path('score',views.Session, name = 'session'),
    path('score',views.Recompensas, name = 'recompensas'),
    path('score',views. Try, name = 'try'),
    '''
