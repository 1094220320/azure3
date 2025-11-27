from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("hola mundo")

def hola(request):
    return render(request, "anime.html")

def chao(request):
    return render(request, "1-plantilla.html")