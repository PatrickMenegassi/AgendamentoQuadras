from django.shortcuts import render, redirect, get_object_or_404
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.template.loader import render_to_string
from ..models import Clientes, Agendamento, Quadra
from ..forms import AgendamentoForm

def lista_agendamentos(request):
    
    return render(request, 'agendamentos/lista_agendamentos.html')

def novo_agendamento(request):
    data_selecionada = request.GET.get('data') # Precisa para abrir o forms
    data_obj = datetime.strptime(data_selecionada, '%Y-%m-%d')
    data_formatada = data_obj.strftime('%d/%m/%Y')
    print(request.POST)
    if request.method == 'POST':
        post_data = request.POST.copy()
        
        if not post_data.get('data'):
            post_data['data'] = agendamento.data.isoformat()

        form = AgendamentoForm(post_data)
        if form.is_valid():
            form.save()
            agendamento = form.save()
            return JsonResponse({'success': True, 'id': agendamento.id})
        else:
            return JsonResponse({'success': False, 'id': 'Dados Inválidos'})
    else:
        form = AgendamentoForm(initial={'data': data_selecionada})
        data_selecionada = request.GET.get('data', '')
        
        # Gera o token manualmente
        csrf_token = get_token(request)
        
        return render(request, 'agendamentos/modal_agendamento.html', {
            'form': form,
            'data_selecionada': data_selecionada,
            'csrf_token': csrf_token,  # Passa o token manualmente
            'data_titulo': data_formatada,
            'url_direcionada': 'novo_agendamento'
        })


def mostra_agendamentos(request):

    cores_quadras = {
        'Quadra Areia 1': "#F800AE",  
        'Quadra Areia 2': "#FF0000",  
        'Quadra Areia 3': "#00D0FF", 
        'Quadra Areia 4': "#00FF88",  
        'Quadra Society': "#FFC400",  
    }
    
    agendamentos = Agendamento.objects.all()
    
    events = []
    for agendamento in agendamentos:
        cor = cores_quadras.get(agendamento.quadra.nome_quadra, '#3788D8')  # Cor padrão
        events.append({
            'title': f"{agendamento.cliente.nome} - {agendamento.quadra.nome_quadra}",
            'start': f"{agendamento.data}T{agendamento.hora_inicio}",
            'end': f"{agendamento.data}T{agendamento.hora_fim}",
            'color': cor,  # ⭐ COR PERSONALIZADA
            'textColor': '#000000',  # Cor do texto
            'id': agendamento.id,
        })
    
    return JsonResponse(events, safe=False)

def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    data_selecionada = request.GET.get('data')
    
    
    if request.method == 'POST':
        post_data = request.POST.copy()
        
        if not post_data.get('data'):
            post_data['data'] = agendamento.data.isoformat()
        
        form = AgendamentoForm(post_data, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(initial={'data': data_selecionada}, instance=agendamento)
    
    return render(request, 'agendamentos/modal_agendamento.html', {
        'form': form,
        'data_selecionada': data_selecionada,
        'agendamento': agendamento,
        'data_titulo': agendamento.data.strftime('%d/%m/%Y'),
        'url_direcionada': 'editar_agendamento'
    })