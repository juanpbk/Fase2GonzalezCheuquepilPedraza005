from django.shortcuts import render
from . models import Juego, Compañia
from django.views import generic

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
