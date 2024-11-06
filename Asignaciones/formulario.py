from django import forms
from .models import Horario_y_materia

class HorarioForm(forms.ModelForm):
    hora_inicio = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    hora_fin = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Horario_y_materia
        fields = '__all__'
