from django.shortcuts import render
from main.models import Oferta
# Create your views here.

def lista_oferta(request):
    lista = Oferta.objects.all()
    dicionario = { 'lista' :  lista, 'contador': 10 }
    return render(request,'main/lista.html', dicionario )