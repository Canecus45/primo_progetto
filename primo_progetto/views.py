from django.shortcuts import render


def index_root(request):
    return render(request, "primo_progetto/templates/index_root.html")
