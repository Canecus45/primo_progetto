from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Corsi
# Create your views here.

def corsi_formazione_index(request):
    return render(request, "corsi_formazione_index.html")

def lista_corsi(request):
    Titoli=Corsi.objects.all()
    context={
        'Corsi':Titoli,
    }
    return render(request,'lista_corsi.html',context)
def dettagli_corsi(request):
    corso = get_object_or_404(corso)
    context = {"Corso": corso}
    return render(request, "dettagli_corso.html", context)
def corsi_dopo(request):
    #corsi che iniziano solo dopo 01/05/2025
    for corso in Corsi:
        if corso.data_inzio>=01/05/2025:
            context={'Corso':corso.titolo}
    return render(request,"corsi_dopo.html",context)
def corsi_meno(request):
    #corsi con <= di 20 posti
    for corso in Corsi:
        if corso.posti<=20:
            context={'Corso':corso.titolo}
    return render(request,"corsi_meno.html",context)
def corsi_terminano_entro(request):
    #corsi che termino entro il 30/04/2025
    for corso in Corsi:
        if corso.data_fine<=30/04/2025:
            context={'Corso':corso.titolo}
    return render(request,"corsi_dopo.html",context)