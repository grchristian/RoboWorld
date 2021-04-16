from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('index',views.index, name = 'index'),
    path('', views.inicio, name="inicio"),
    path('stats/', views.stats, name="stats"),
    path('micuenta/', views.micuenta, name="micuenta"),
    path('juego_unity/', views.juego_unity, name="juego_unity"),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion")
]

'''
    path('login/', views.login, name="login"),
    path('logged_out/', views.logged_out, name="logged_out"),
    path('score/', views.score, name="score"),
    '''
