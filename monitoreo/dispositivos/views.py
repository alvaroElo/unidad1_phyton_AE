from django.shortcuts import render
# Create your views here.
def inicio(request):
    Titulo = {"nombre": "Eco energy consumo Status"}
    Dispositivos = [
        {"nombre": "sensor 1", "consumo": 60},
        {"nombre": "maquina 2", "consumo": 200},
        {"nombre": "maquina prueba4", "consumo": 100}
    ]

    max_consumo = 100


    return render(request, "dispositivos/inicio.html",{
        "Titulo": Titulo,
        "Dispositivos": Dispositivos,
        "max_consumo" : max_consumo
        })