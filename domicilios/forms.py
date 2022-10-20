from django.forms import  ModelForm, TextInput

from personas.models import Domicilio


class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle': TextInput(attrs={'type':'number'})
        }