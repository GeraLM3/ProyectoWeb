from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST": #Si se ha hecho POST, debe rescatar la info del formulario
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django", "El usuario con nombre {} con la direccion {} te escribe lo siguiente:\n\n {}".format(nombre,email,contenido),"", ["gerardo.lmm3@gmail.com"], reply_to = [email]) ##No funciona ahora mismo pero si verifica la validacion del formulario

            try:
                email.send()
                return redirect("/contacto/?valido") #El simbolo ? es como se pasa la info desde GET
            except:
                return redirect("/contacto/?novalido")

    return render(request, "Contacto/contacto.html", {'miFormulario': formulario_contacto})