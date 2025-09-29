from django.db import models

class Clientes(models.Model):
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
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'