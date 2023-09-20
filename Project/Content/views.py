from django.shortcuts import render

def home(request):
    return render(request, "Content/home.html")

def leistungen(request):
    return render(request, "Content/leistungen.html")

def kontakt(request):
    return render(request, "Content/kontakt.html")

def impressum(request):
    return render(request, "Content/impressum.html")