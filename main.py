from paquete1.modulo1 import *
from paquete1.modulo2 import *

cliente1 = Client("Juan","juanrago2000@gmail.com",30,"+49-2494542379")

compra1 = cliente1.comprar("Sandia")
if compra1 is not None:
    print( "\nLa compra fue exitosa : ")
    for dato in compra1:
        print( "\t" + dato + " = " + str(compra1[dato]))

compra2 = cliente1.comprar("Manzana","12")
if compra2 is not None:
    print( "\nLa compra fue exitosa : ")
    for dato in compra2:
        print( "\t" + dato + " = " + str(compra2[dato]))

compra3 = cliente1.comprar("Anana",2)
if compra3 is not None:
    print( "\nLa compra fue exitosa : ")
    for dato in compra3:
        print( "\t" + dato + " = " + str(compra3[dato]))

compra4 = cliente1.comprar("Manzana",6)
if compra4 is not None:
    print( "\nLa compra fue exitosa : ")
    for dato in compra4:
        print( "\t" + dato + " = " + str(compra4[dato]))

compra5 = cliente1.comprar("Manzana","2w")
if compra5 is not None:
    print( "\nLa compra fue exitosa : ")
    for dato in compra5:
        print( "\t" + dato + " = " + str(compra5[dato]))

print( "\nCantidad historica de total de Manzanas compradas = " + str(cliente1.cant_producto_comprados("Manzana")) + "\n")

print( "\nCantidad historica de total de Melones comprados = " + str(cliente1.cant_producto_comprados("Melon")) + "\n")


ultima_compra = cliente1.obtener_ult_compra();
print( "\nLa última compra del cliente es : \n")
for dato in ultima_compra:
    print( "\t" + dato + " = " + str(ultima_compra[dato]))


"""
#correspondiente al modulo2 (pre-entrega1)

crear_registro() # Se crea un registro

mostrar_datos() # Se imprime todos los datos de los usuarios

login() # Ejecución del procedimiento de logeo
"""