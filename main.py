from package1.module1 import *
from package1.module2 import *

client1 = Client("Juan","juanrago2000@gmail.com",30,"+49-2494542379")
print(client1 + "\n")

purchase1 = client1.buy("Sandia")
if purchase1 is not None:
    print( "\nLa compra fue exitosa : ")
    for data in purchase1:
        print( "\t" + data + " = " + str(purchase1[data]))

purchase2 = client1.buy("Manzana","12")
if purchase2 is not None:
    print( "\nLa compra fue exitosa : ")
    for data in purchase2:
        print( "\t" + data + " = " + str(purchase2[data]))

purchase3 = client1.buy("Anana",2)
if purchase3 is not None:
    print( "\nLa compra fue exitosa : ")
    for data in purchase3:
        print( "\t" + data + " = " + str(purchase3[data]))

purchase4 = client1.buy("Manzana",6)
if purchase4 is not None:
    print( "\nLa compra fue exitosa : ")
    for data in purchase4:
        print( "\t" + data + " = " + str(purchase4[data]))

purchase5 = client1.buy("Manzana","2w")
if purchase5 is not None:
    print( "\nLa compra fue exitosa : ")
    for data in purchase5:
        print( "\t" + data + " = " + str(purchase5[data]))

print( "\nCantidad historica de total de Manzanas compradas = " + str(client1.number_product_purchased("Manzana")) + "\n")

print( "\nCantidad historica de total de Melones comprados = " + str(client1.number_product_purchased("Melon")) + "\n")

last_purchase = client1.get_last_purchase();
print( "\nLa última compra del cliente es : \n")
for data in last_purchase:
    print( "\t" + data + " = " + str(last_purchase[data]))

"""
#correspondiente al modulo2 (pre-entrega1)

crear_registro() # Se crea un registro

mostrar_datas() # Se imprime todos los datas de los usuarios

login() # Ejecución del procedimiento de logeo
"""