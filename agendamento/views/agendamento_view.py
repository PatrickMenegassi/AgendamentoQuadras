from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from ..models import Clientes, Agendamento, Quadra
from ..forms import AgendamentoForm

def lista_agendamentos(request):
    
    return render(request, 'agendamentos/lista_agendamentos.html')

def novo_agendamento(request):
    data_selecionada = request.GET.get('data')
    
    form = AgendamentoForm(initial={'data': data_selecionada})
    
    # Renderiza apenas o modal com o form
    html = render_to_string('agendamentos/modal_agendamento.html', {
        'form': form,
        'data_selecionada': data_selecionada
    })
    
    return HttpResponse(html)


def mostra_agendamentos(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    
    agendamentos = Agendamento.objects.all()
    
    events = []
    for agendamento in agendamentos:
        events.append({
            'title': f"{agendamento.cliente.nome} - {agendamento.quadra.nome_quadra}",
            'start': f"{agendamento.data}T{agendamento.hora_inicio}",
            'end': f"{agendamento.data}T{agendamento.hora_fim}",
            'id': agendamento.id,
        })
    
    return JsonResponse(events, safe=False)