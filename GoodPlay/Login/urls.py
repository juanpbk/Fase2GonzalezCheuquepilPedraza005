from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('consolas/', views.consolas, name='consolas.html'),
    path('juegos/', views.juegos, name='juegos.html'),
    path('computacion/', views.computacion, name='computacion.html'),
    path('accesorio/', views.accesorio, name='accesorio.html'),
]

