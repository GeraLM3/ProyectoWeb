from django.shortcuts import redirect, render
from .carro import Carro
from Tienda.models import Producto
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)
    if request.META['HTTP_REFERER'] == 'http://127.0.0.1:8000/tienda/carroweb':
        return redirect("Carro")
    else:
        return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto = producto)
    return redirect("Carro")

def eliminar_productos(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto = producto)
    total3 = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total3 = total3+(float(value["cantidad"]))
    else:
        total3 = "Debes hacer login."
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto = producto)
    return redirect("Carro")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")

