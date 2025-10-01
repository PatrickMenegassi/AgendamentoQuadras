from django.db import models
from datetime import datetime

class Clientes(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    nome = models.CharField(
        max_length=100
    )

    telefone = models.CharField(
        max_length=11
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=True
    )

    data_nascimento = models.DateField()

    email = models.EmailField(
        blank=True, 
        null=True
    )

    endereco = models.CharField(
        max_length=200, 
        blank=True, 
        null=True
    )

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome
    
    def telefone_formatado(self):
        t = self.telefone
        if len(t) == 11:
            return f"({t[:2]}) {t[2:7]}-{t[7:]}"
    
    def data_nascimento_formatada(self):
        return self.data_nascimento.strftime('%d/%m/%Y')
