from django import forms
from ..models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'telefone', 'cpf', 'data_nascimento', 'email']

    nome = forms.CharField(
        label='Nome Completo *',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome completo',
            'autofocus': True
        }),
        error_messages={
            'required': 'O nome é obrigatório',
            'max_length': 'Nome muito longo (máx. 100 caracteres)'
        }
    )
    
    cpf = forms.CharField(
        label='CPF *',
        max_length=14,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '000.000.000-00',
            'data-mask': '000.000.000-00'
        }),
        error_messages={
            'required': 'O CPF é obrigatório'
        }
    )
    
    telefone = forms.CharField(
        label='Telefone *',
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(11) 99999-9999',
            'data-mask': '(00) 00000-0000'
        }),
        error_messages={
            'required': 'O telefone é obrigatório'
        }
    )
    
    email = forms.EmailField(
        label='E-mail',
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        }),
        error_messages={
            'invalid': 'Digite um e-mail válido'
        }
    )
    
    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        error_messages={
            'invalid': 'Digite uma data válida'
        }
    )
    
    endereco = forms.CharField(
        label='Endereço',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Rua, número, bairro, cidade...',
            'rows': 3
        }),
        error_messages={
            'max_length': 'Endereço muito longo'
        }
    )
    
    ativo = forms.BooleanField(
        label='Cliente ativo',
        required=True,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            raise forms.ValidationError("CPF deve ter 11 dígitos")
        
        # Aqui você pode adicionar validação de CPF real se quiser
        # if not self.validar_cpf(cpf):
        #     raise forms.ValidationError("CPF inválido")
        
        return cpf
    
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        telefone = ''.join(filter(str.isdigit, telefone))
        
        if len(telefone) not in [10, 11]:
            raise forms.ValidationError("Telefone deve ter 10 ou 11 dígitos")
        
        return telefone
    
    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data['data_nascimento']
        
        if data_nascimento:
            from django.utils import timezone
            if data_nascimento > timezone.now().date():
                raise forms.ValidationError("Data de nascimento não pode ser futura")
        
        return data_nascimento
