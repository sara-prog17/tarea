from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def index(request):
    return render(request,'index.html',{})

def inicio(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        # GUARDAR LA INFORMACION
        else:
            return redirect('inicio')
        
 
    else:
        formulario = ClienteForm()
        return render(request, 'inicio.html', {'formulario': formulario})


def inicioP(request):   
    if request.method == 'POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicioP')
       
        else:
            return redirect('inicioP')
 
    else:
        formulario = PedidoForm()
        return render(request, 'inicioP.html', {'formulario': formulario})

def lista(request):
    cliente= Cliente.objects.all()
    return render(request, 'lista.html',{'cliente': cliente})

def listaP(request):
    pedido= Pedido.objects.all()
    return render(request, 'listaP.html',{'pedido': pedido})


def ActualizarC(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect ('lista')
    else:
        formulario = ClienteForm(instance = cliente)
        return render(request,'inicio.html', {'formulario':formulario, 'id': id} )

def ActualizarP(request, id):
    pedido = Pedido.objects.get(n_pedido=id)
    if request.method == 'POST':
        formulario = PedidoForm(request.POST, instance = pedido)
        if formulario.is_valid:
            formulario.save()
            return redirect ('listaP')
    else:
        formulario = PedidoForm(instance = pedido)
        return render(request,'inicioP.html', {'formulario':formulario, 'id': id} )

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('lista')
    
def eliminarP(request, id):
    pedido = Pedido.objects.get(n_pedido=id)
    pedido.delete()
    return redirect('listaP')