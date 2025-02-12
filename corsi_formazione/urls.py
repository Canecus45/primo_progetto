from django.urls import path
from .views import corsi_formazione_index,lista_corsi,dettagli_corsi,corsi_meno,corsi_terminano_entro

app_name="corsi_formazione"

urlpatterns = [
    path('corsi_formazione_index', corsi_formazione_index , name='corsi_formazione_index'),
    path('lista_corsi', lista_corsi,name="lista_corsi"),
    path('dettagli_corsi', dettagli_corsi,name="dettagli_corsi"),
    path('corsi_meno', corsi_meno,name="corsi_meno"),
    path('corsi_termiano_entro', corsi_terminano_entro,name="corsi_termiano_entro"),
    # View non fatta statistiche avaznate
    path('statistiche_avanzate', lista_corsi,name="lista_corsi"),
]
