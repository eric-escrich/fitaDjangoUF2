from django.shortcuts import render
from lloguer.models import Automobil

def lista_automobils(request):
    automobils = Automobil.objects.all()
    return render(request, 'llistar-automobils.html', {'automobils': automobils})
