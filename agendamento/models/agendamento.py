from django.db import models
from .cliente import Clientes
from .quadra import Quadra

class Agendamento(models.Model):
    cliente = models.ForeignKey(
        Clientes, 
        on_delete=models.CASCADE
        )

    telefone = models.CharField(
        max_length=15, 
        blank=True, 
        null=True
        )
    
    quadra = models.ForeignKey(
        Quadra,
        on_delete=models.CASCADE
    )

    data = models.DateField()

    hora_inicio = models.TimeField()

    hora_fim = models.TimeField()


    class Meta:
        unique_together = [['quadra', 'data', 'hora_inicio']]

    def __str__(self):
        return f"{self.nome_cliente} - {self.data} {self.hora_inicio}"
