from django.db import models

# Create your models here.

class Corsi(models.Model):
    titolo=models.CharField(max_length=100)
    descrizione=models.TextField()
    data_inizio=models.DateField()
    data_fine=models.DateField()
    posti_disponibili=models.IntegerField()

    class Meta:
        verbose_name="Corso"
        verbose_name_plural="Corsi"