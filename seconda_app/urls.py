from django.urls import path
from .views import index2, es_if, es_if_else_elif

app_name = "seconda_app"

urlpatterns = [
    path("index2", index2, name="index2"),
    path("es_if", es_if, name="es_if"),
    path("es_if_else_elif", es_if_else_elif, name="es_if_else_elif"),
]
