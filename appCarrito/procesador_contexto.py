def total_carrito(request):
    total = 0
    cantidad=0
    if 'carrito' in request.session.keys():
        for key, value in request.session['carrito'].items():
            total += value['subtotal']
            cantidad += value['cantidad']
    return {'total_carrito': total, 'cantidadProd':cantidad}


