from django.db import models
from datetime import datetime

# Create your models here.

class Evento(models.Model):
    titolo=models.CharField(max_length=200)
    descrizione=models.TextField()
    data_inizio=models.DateField(auto_now=False, auto_now_add=False)
    data_fine=models.DateField(auto_now=False, auto_now_add=False)
    posti_disponibili=models.IntegerField()
    
    def __str__(self):
        return self.titolo

    def Meta():
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventi'