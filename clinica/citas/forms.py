from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            'paciente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del paciente'
                }
            ),
            'doctor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del doctor'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
            'motivo': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Motivo de la cita',
                    'rows': 4
                }
            ),
        }
