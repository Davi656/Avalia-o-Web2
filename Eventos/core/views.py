from django.http import HttpResponse
from datetime import datetime

acessos = 0

def ola(request):
    return HttpResponse("Olá Mundo")

def mes(request):
    global acessos
    acessos += 1

    mes_atual = datetime.now().month
    return HttpResponse(f"Mês atual: {mes_atual}")

def acessos_view(request):
    global acessos
    acessos += 1

    return HttpResponse(f"Número de acessos: {acessos}")

def oversize(request):
    global acessos
    acessos += 1

    if acessos > 10:
        return HttpResponse("sim")
    else:
        return HttpResponse("não")