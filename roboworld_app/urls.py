from django.urls import path, include
from . import views


urlpatterns = [
    #---------------------- URLS LISTOS Y TRABAJANDO ----------------------
    path('', views.inicio, name="inicio"),
    path('juego_unity/', views.juego_unity, name="juego_unity"),
    path('cuenta_usuario',views.cuenta_usuario, name = 'cuenta_usuario'),
    #---------------------- URLS LISTOS Y TRABAJANDO ----------------------

    url(r'^register/$', views.register, name='register'),
    url(r'^password-change-done/$',auth_views.password_change_done,{'template_name': 'cadmin/password_change_done.html'},name='password_change_done'),


    #------------------------------ GRÁFICAS ------------------------------
    path('grafica1/', views.grafica1, name="grafica1"),
    path('grafica2/', views.grafica2, name="grafica2"),
    #------------------------------ GRÁFICAS ------------------------------

    
    path('proceso',views.proceso, name = 'proceso'),
    path('datos',views.datos, name = 'datos'),
    path('buscaJugadorBody', views.buscaJugadorBody, name='buscaJugadorBody'),
    path('ejemploSQL', views.ejemploSQL, name='ejemploSQL'),
    path('score',views.score, name = 'score'),
    path('level',views.Level, name = 'level'),
    path('engranes',views.engranes, name = 'engranes'),
    path('sesion',views.sesion, name = 'sesion'),
    path('recompensas',views.recompensas, name = 'recompensas'),
    path('prueba',views.prueba, name = 'prueba'),

    #ejemplos clase
    path('index2',views.index2, name = 'index2'),
    path('proceso2',views.proceso2, name = 'proceso2')
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

