from django import forms
from .models import Consumidor


class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = ['email', 'nome']