from django import forms
from .models import Produto, Emprestimo, Consumidor

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'quantidade', 'descricao')

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['consumidor', 'produto', 'quantidade']

class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['email', 'nome']