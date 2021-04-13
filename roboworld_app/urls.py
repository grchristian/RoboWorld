from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('stats/', views.stats, name="stats"),
    path('micuenta/', views.micuenta, name="micuenta"),
    path('juego_unity/', views.juego_unity, name="juego_unity"),

    path('login/', views.login, name="login"),
    path('logged_out/', views.logged_out, name="logged_out"),
    path('score/', views.score, name="score"),
]

