from django.shortcuts import render

# Create your wiews


def homepage(request):
    return render(request, "homepage.html")  # Corrected path


def welcome(request):
    return render(request, "welcome.html")


def lista(request):
    return render(request, "lista.html")


def chi_siamo(request):
    return render(request, "chi_siamo.html")
