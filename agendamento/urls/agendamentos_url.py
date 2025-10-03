from django.urls import path
from ..views.agendamento_view import lista_agendamentos, novo_agendamento, mostra_agendamentos

urlpatterns = [
    path('agendamentos/', lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', novo_agendamento, name='novo_agendamento'),
    path('agendamentos/mostraagendamentos/', mostra_agendamentos, name='mostra_agendamentos'),
    #path('clientes/excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
]