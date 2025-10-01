from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from ..models import Clientes, Agendamento, Quadra

def lista_agendamentos(request):
    
    return render(request, 'agendamentos/lista_agendamentos.html')

def novo_agendamento(request):
    clientes = Clientes.objects.filter(ativo=True).values('id', 'nome')
    quadras = Quadra.objects.all().values('id', 'nome_quadra', 'valor_hora')
    
    data = {
        'clientes': list(clientes),
        'quadras': list(quadras),
    }
    
    return JsonResponse(data)