from django.shortcuts import get_object_or_404, redirect, render

from personas.models import Domicilio
from domicilios.forms import DomicilioForm

# Create your views here.
def verDomicilio(request):
    domicilios = Domicilio.objects.all()
    return render(request, 'domicilios.html', {'domicilios': domicilios})

def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'dom_detalle.html', {'domicilio':domicilio}) 

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilio')
           
    else:
        formaDomicilio = DomicilioForm()
    
    return render(request, 'dom_nuevo.html', {'formaDomicilio': formaDomicilio})

def editarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST,instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilio')
           
    else:
        
        formaDomicilio = DomicilioForm(instance=domicilio)
    
    return render(request, 'dom_editar.html', {'formaDomicilio': formaDomicilio})

def eliminarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('domicilio')   