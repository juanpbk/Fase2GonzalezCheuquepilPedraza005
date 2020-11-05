from django.shortcuts import render
from . models import Juego, Compañia
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    num_Juego = Juego.objects.all().count()
    num_Juego_available=Juego.objects.filter(juego__exact='E').count()
    num_compañias = Compañia.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_Juego': num_Juego, 
        'num_Juego_available': num_Juego_available, 'num_compañias' : num_compañias}, 
    )
def consolas(request):
    
    return render(
        request,
        'consolas.html',
    )

def juegos(request):
    
    return render(
        request,
        'juegos.html',
    )

def accesorio(request):
    
    return render(
        request,
        'accesorio.html',
    )

def computacion(request):
    
    return render(
        request,
        'computacion.html',
    )

class JuegoCreate(CreateView):
    model = Juego
    fields = '__all__'

class JuegoUpdate(UpdateView):
    model = Juego
    fields = ['codigo,nombre,compañia,fecha']

class JuegoDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy('juegos')

class JuegoDetailView(generic.DetailView):
    model = Juego





