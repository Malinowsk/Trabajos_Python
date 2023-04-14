from package1.client import *
from package1.pre_delivery_1 import *


client1 = Client("Rafael","rafa@gmail.com",21,"+49-2494541212")

print( f"\n\n////////////////////// Ejemplo Cliente {client1.name} ///////////////////////////\n")

print(f"\n{client1}\n")

purchase1 = client1.buy(product="Sandia", price = 30.99)

print( f"\nDatos de la compra realizada por {client1.name}: ")
for data in purchase1:
    print( "\t" + data + " = " + str(purchase1[data]))

purchase2 = client1.buy(product="Manzana", price= 5.00 , number= "12")

print( f"\nDatos de la compra realizada por {client1.name} : ")
for data in purchase2:
    print( "\t" + data + " = " + str(purchase2[data]))

purchase3 = client1.buy(product= "Anana", price= 55.90)

print( f"\nDatos de la compra realizada por {client1.name} : ")
for data in purchase3:
    print( "\t" + data + " = " + str(purchase3[data]))

purchase4 = client1.buy(product="Manzana", price= 5.00 , number= 6)

print( f"\nDatos de la compra realizada por {client1.name} : ")
for data in purchase4:
    print( "\t" + data + " = " + str(purchase4[data]))


print( "\nCantidad historica de total de manzanas compradas por " + str(client1.name) + " = " + str(client1.number_product_purchased("Manzana")) + "\n")

print( "\nCantidad historica de total de melones comprados por " + str(client1.name) + " = " + str(client1.number_product_purchased("Melon")) + "\n")

last_purchase = client1.get_last_purchase();
if last_purchase != None:
    print( f"\nLa última compra del cliente {client1.name} es : \n")
    for data in last_purchase:
        print( "\t" + data + " = " + str(last_purchase[data]))
else:
    print( f"\nEl cliente {client1.name} no ha realizado compras : \n")



client2 = Client("Juan","juanrago2000@gmail.com",30,"+49-2494542379")

print( f"\n\n////////////////////// Ejemplo Cliente {client2.name} ///////////////////////////")

print(f"\n\n{client2}\n")

print( "\nCantidad historica de total de manzanas compradas por " + str(client2.name) + " = " + str(client2.number_product_purchased("Manzana")) + "\n")

print( "\nCantidad historica de total de peras comprados por " + str(client2.name) + " = " + str(client2.number_product_purchased("Melon")) + "\n")

last_purchase = client2.get_last_purchase();
if last_purchase != None:
    print( f"\nLa última compra del cliente {client2.name} es : \n")
    for data in last_purchase:
        print( "\t" + data + " = " + str(last_purchase[data]))
else:
    print( f"\nEl cliente {client2.name} no ha realizado compras. \n")



"""
#correspondiente a pre_delivery_1.py (pre-entrega1)

create_register() # Se crea un registro

show_data() # Se imprime todos los datos de los usuarios

login() # Ejecución del procedimiento de logeo

"""