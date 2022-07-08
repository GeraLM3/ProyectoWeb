class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": (str(producto.precio)),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
    
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]-1
                    value["precio"] = float(value["precio"]) - producto.precio
                    if value["cantidad"] < 1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

#Cuando el usuario entra por primera vez a manejar el carro, agrega un articulo por primera vez,
#iguala la sesion del usuario con ese carro, si el usuario se va, al volver, comprobar que la sesion es la misma, en caso de que no tenga carro debera crearlo, si crea el carro y vuelve a la misma, debe usar el mismo carro que tenia iniciado antes