from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('consolas/', views.consolas, name='consolas.html'),
    path('juegos/', views.juegos, name='juegos.html'),
    path('computacion/', views.computacion, name='computacion.html'),
    path('accesorio/', views.accesorio, name='accesorio.html'),
    path('juegos/<str:pk>',views.JuegoDetailView.as_view(), name='juegos-detail'),
    path('juego_list/', views.JuegoListView.as_view(), name='juego_list'),
    path('juego/<int:pk>', views.JuegoListView.as_view(), name='juego-detail'),
]


urlpatterns+=[
    path('juegos/create/', views.JuegoCreate.as_view(), name='juego_create'),
    path('juegos/<str:pk>/update/', views.JuegoUpdate.as_view(), name='juego_update'),
    path('juegos/<str:pk>/delete/', views.JuegoDelete.as_view(), name='juego_delete'),


]