from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest
from .models import Evento

# Create your views here.

def query_a(request):
    # Prima richiesta
    query_a=Evento.objects.order_By("-Data Inizio").first()

    context = {
        'query_a':query_a
    }

    return render(request, "query_a.html", context)

def query_b(request):
    # Seconda richiesta
    query_b=Evento.objects.all()

    context = {
        'query_b':query_b
    }

    return render(request, "query_b.html",context)

def query_c(request):
    # Terza richiesta
    query_c = Evento.objects.filter(data_inizio=datetime.date(2025,6,1))
    context = {
                "query_c": query_c,
            }
    return render(request, "query_c.html", context)

def query_d(request):
    # Quarta richeista
    query_d = Evento.objects.filter(posti_disponibili=80)
    context = {
                "query_d": query_d,
            }
    return render(request, "query_d.html", context)

def query_e(request):
    # Quinta richiesta
    query_e = Evento.objects.filter(data_fine=datetime.date(2025,4,30))
    context = {
                "query_e": query_e,
            }
    return render(request, "query_e.html", context)

def query_f(request):
    # Sesta richeista
    evento_piu_posti = Evento.objects.order_by('posti_disponibili').first()
    evento_meno_posti = Evento.objects.order_by('posti_disponibili').first()
    
    totale_posti=0
    eventi = Evento.objects.all()
    for evento in eventi:
        totale_posti+=evento.posti_disponibili

    context = {
                "evento_più_posti": evento_piu_posti,
                "evento_meno_posti": evento_meno_posti,
                "totale_posti": totale_posti,
            }
    return render(request, "query_f.html", context)