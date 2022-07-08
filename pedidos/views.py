from email import message
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido
from django.contrib import messages


# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido) #Muchas instrucciones de insert input
    #enviar_mail(
        #pedido = pedido,
        #lineas_pedido = lineas_pedido
        #nombre_usuario = request.username,
        #email_usuario = request.usermail
    #)
    #messages.success(request, "El pedido se ha creado correctamente")

    #return redirect("../tienda")