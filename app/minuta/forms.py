from django import forms
from .models import MinutasCasei

class FormMinutaCasei(forms.ModelForm):
    class Meta:
        model = MinutasCasei
        fields = '__all__'

        widgets = {
            'titulominuta': forms.TextInput(attrs={'class': 'form-control', 
                                                   'style': 'width: 300px;', 
                                                   'placeholder': 'Ingrese el título de la minuta'}),
            'fechaminuta': forms.DateInput(attrs={'class': 'form-control', 
                                                  'style': 'width: 300px;', 
                                                  'type': 'date'}),
            'minuta': forms.Textarea(attrs={'class': 'form-control', 
                                            'style': 'width: 300px; height: 100px;', 
                                            'placeholder': 'Escriba la minuta aquí'}),
            'acuerdos': forms.Textarea(attrs={'class': 'form-control', 
                                              'style': 'width: 300px; height: 100px;', 
                                              'placeholder': 'Escriba los acuerdos aquí'}),
        }

