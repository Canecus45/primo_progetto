from django.urls import path
from .views import home,articoloDetailView

app_name='news'

urlpatterns = [
    path('',home,name="homewiew"),
    path('articoli/<int:pk>',articoloDetailView,name="Articolo_detail"),
]
