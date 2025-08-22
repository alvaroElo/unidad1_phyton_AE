from django.shortcuts import render
# Create your views here.
def inicio(request):
    contexto = {"nombre": "Hola Mundo Az"}
    productos = [
        {"nombre": "sensor 1", "valor": 100}
        {"nombre": "sensor 2", "valor": 200}
        {"nombre": "sensor 3", "valor": 1300}
    ]




    return render(request, "dispositivos/inicio.html",{
        "contexto": contexto,
        "productos": productos
        })