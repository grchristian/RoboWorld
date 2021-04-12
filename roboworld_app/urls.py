from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('stats/', views.stats, name="stats"),
    path('micuenta/', views.micuenta, name="micuenta"),
]

