from django.urls import path
from ..views.cliente_view import *

urlpatterns = [
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/novo/', novo_cliente, name='novo_cliente'),
    path('clientes/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
]