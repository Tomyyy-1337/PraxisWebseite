from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Leistungen", views.leistungen, name="leistungen"),
    path("Kontakt", views.kontakt, name="kontakt"),
    path("Impressum", views.impressum, name="impressum"),
]