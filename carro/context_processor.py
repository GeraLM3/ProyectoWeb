def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total+(float(value["precio"]))
    else:
        total = "Debes hacer login."
    return {"importe_total_carro": total}

def producto_total_carro(request):
    total2 = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total2 = total2+(int(value["cantidad"]))
    else:
        total2 = "Debes hacer login."
    return {"producto_total_carro": total2}