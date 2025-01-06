from .cart import Cart

# crea procesador de contexto lo que permite agregar datos a todas las plantillas renderizadas

def cart(request):
    return{'cart': Cart(request)}