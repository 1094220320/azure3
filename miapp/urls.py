from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.saludo,),
    path("principal/", views.hola, name="principal"),
    path("secundario/", views.chao, name="secundario"),
]