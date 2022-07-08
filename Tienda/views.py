from django.shortcuts import render
from .models import Producto
from django.db.models import Sum

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()[::-1]
    return render(request, "Tienda/tienda.html", {"productos": productos})

def carroweb(request):
    productos = Producto.objects.all()[::-1]
    return render(request, "Carroweb/carroweb.html", {"productos": productos})
