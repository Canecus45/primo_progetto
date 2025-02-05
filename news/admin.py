from django.contrib import admin
from .models import Giornalista, Articolo

admin.site.register(Articolo)
admin.site.register(Giornalista)

# Register your models here.
