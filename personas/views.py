from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from personas.models import Persona

# Create your views here.
def detallePersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'detalle.html', {'persona':persona})

PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
           
    else:
        formaPersona = PersonaForm()
    
    return render(request, 'nuevo.html', {'formaPersona': formaPersona})