from django import forms
from .models import *

class InscripcionForm (forms.ModelForm):

    class Meta:
        model = formulario

        fields = '__all__'


        widgets = {
            'id':forms.TextInput(attrs={'style':'display:none'}),
			'acompanado': forms.Select(attrs={'onChange':'compania()'}),
			'celula': forms.Select(attrs={'onChange':'esta_en_celula()'}),
			'nacimiento':forms.TextInput(attrs={'type':'date','class':'form-control','placeholder':'dd/mm/aaaa'}),
            'parentesco': forms.Select(attrs={'class':'form-control','style':'display: none; width:100% !important'}),
            'nombre_compania': forms.TextInput(attrs={'class':'form-control','style':'display: none;'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control','style':'width: 100%;'}),
            'edad': forms.TextInput(attrs={'class':'form-control','placeholder':' A partir de 13 y hasta 35 años'}),
		}
		