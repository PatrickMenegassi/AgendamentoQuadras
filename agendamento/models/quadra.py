from django.db import models

class Quadra(models.Model):
    nome_quadra = models.CharField(
        max_length=100
    )

    valor_hora = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.nome_quadra}"
    
    class Meta:
        verbose_name = 'Quadra'
        verbose_name_plural = 'Quadras'