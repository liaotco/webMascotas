def total_carrito(request):
    total = 0
    if 'carrito' in request.session.keys():
        for key, value in request.session['carrito'].items():
            total += value['subtotal']
    return {'total_carrito': total}


def cuantos_productos(request):
    cantidad=0
    for key,value in request.session['carrito'].items():
        cantidad +=1
    return{'productos_carrito':cantidad}