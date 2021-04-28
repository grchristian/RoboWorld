from django.urls import path, include
from . import views


urlpatterns = [
    #---------------------- URLS LISTOS Y TRABAJANDO ----------------------
    path('', views.inicio, name="inicio"),
    path('juego_unity/', views.juego_unity, name="juego_unity"),
    path('cuenta_usuario',views.cuenta_usuario, name = 'cuenta_usuario'),
    #---------------------- URLS LISTOS Y TRABAJANDO ----------------------

    path('register/', views.register, name='register'),


    #------------------------------ GRÁFICAS ------------------------------
    path('grafica1/', views.grafica1, name="grafica1"),
    path('grafica2/', views.grafica2, name="grafica2"),
    path('graficaExito/', views.graficaExito, name="graficaExito"),
    path('graficaMinimo/', views.graficaMinimo, name="graficaMinimo"),
    path('graficaMaximo/', views.graficaMaximo, name="graficaMaximo"),
    path('graficaNiveLlego/', views.graficaNiveLlego, name="graficaNiveLlego"),
    path('graficaGenero/', views.graficaGenero, name="graficaGenero"),
    path('graficaTop5/', views.graficaTop5, name="graficaTop5"),
    #------------------------------ GRÁFICAS ------------------------------

    
    path('proceso',views.proceso, name = 'proceso'),
    path('datos',views.datos, name = 'datos'),
    path('buscaJugadorBody', views.buscaJugadorBody, name='buscaJugadorBody'),
    path('ejemploSQL', views.ejemploSQL, name='ejemploSQL'),

    #------------- CONEXIONES
    path('score',views.score, name = 'score'),
    path('level',views.numero_de_level, name = 'level'),
    path('engranes',views.numero_de_engranes, name = 'engranes'),
    path('sesion',views.num_de_sesion, name = 'sesion'),
    path('recompensas',views.num_de_recompensas, name = 'recompensas'),
    path('prueba',views.num_de_pruebas, name = 'prueba'),
    

    #ejemplos clase
    path('index2',views.index2, name = 'index2'),
    path('proceso2',views.proceso2, name = 'proceso2')
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

