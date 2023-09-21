from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

def home(request):
    if(request.POST.get("Name","") and request.POST.get("Email","") and request.POST.get("Nachricht","")):
        Data = {"nachrichtGesendet": True}
        print(request.POST.get("Nachricht",""))
    else:
        Data = {"nachrichtGesendet": False}
    return render(request, "Content/home.html", Data)

def leistungen(request):
    return render(request, "Content/leistungen.html")

def kontakt(request):
    return render(request, "Content/kontakt.html")

def impressum(request):
    return render(request, "Content/impressum.html")