from django.urls import path
from ..views.agendamento_view import lista_agendamentos, novo_agendamento, mostra_agendamentos, editar_agendamento

urlpatterns = [
    path('agendamentos/', lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', novo_agendamento, name='novo_agendamento'),
    path('agendamentos/mostraagendamentos/', mostra_agendamentos, name='mostra_agendamentos'),
    path('agendamentos/editar/<int:id>/', editar_agendamento, name='editar_agendamento'),
]