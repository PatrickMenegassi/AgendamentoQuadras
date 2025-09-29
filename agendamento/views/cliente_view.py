# agendamento/views/cliente_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Clientes
from ..forms import ClientesForm

def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('lista_clientes')
    else:
        form = ClientesForm()
    
    return render(request, 'clientes/form_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('lista_clientes')
    else:
        form = ClientesForm(instance=cliente)
    
    return render(request, 'clientes/form_cliente.html', {'form': form, 'cliente': cliente})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    cliente.delete()
    messages.success(request, 'Cliente excluído com sucesso!')
    return redirect('lista_clientes')