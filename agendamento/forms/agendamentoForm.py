from django import forms
from ..models import Agendamento, Clientes, Quadra

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'quadra', 'hora_inicio', 'hora_fim']

    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=Clientes.objects.all().order_by('nome'),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control select2-busca',
        }),
    )

    quadra = forms.ModelChoiceField(
        label='Quadra',
        queryset=Quadra.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control select2-busca',
        }),
    )
    
    hora_inicio = forms.TimeField(
        label='Hora de Início *',
        required=True,
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time',
            'placeholder': 'HH:MM'
        }),
    )
    
    hora_fim = forms.TimeField(
        label='Hora de Término *',
        required=True,
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time',
            'placeholder': 'HH:MM'
        }),
    )
