from django.urls import path
from ..views.agendamento_view import *

urlpatterns = [
    path('agendamentos/', lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', novo_agendamento, name='novo_agendamento'),
   # path('clientes/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    #path('clientes/excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
]