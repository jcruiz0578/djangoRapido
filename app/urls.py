from django.urls import path

from app import views

urlpatterns = [
    path("", views.home),
    path("ingreso/", views.ingreso),
    path("registrar/", views.registrar),

    path("edicion/<id>", views.edicion),
]
