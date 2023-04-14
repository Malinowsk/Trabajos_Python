from package1.person import *
import datetime
import random
import string

class Client(Person):

    def __init__(self, name, email, age, phone):
        super().__init__(name, email, age, phone)
        self.shopping = []  # almacenamiento de las compras que realizó el cliente

    def buy(self, product , price ,  number = 1):
        """
        Método para realizar una compra por el cliente.\n 
        Se guarda la compra, la cual contiene un código aleatorio, el producto comprado, 
        precio por unidad, cantidad y fecha de la compra realizada.
        Por último se retorna la compra que fue guardada.\n
        Como parametros se solicita el producto , el precio y opcional la cantidad.
        """
        purchase = { "code" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                    "product" : product ,
                    "price" : float(price), 
                    "number" : int(number), 
                    "date" : datetime.date.today().strftime("%d/%m/%Y") } # fecha actual
        self.shopping.append(purchase) 
        return purchase
   
    def get_last_purchase(self):
        """
        Método para obtener la última compra realizada por el cliente.\n
        De no contener compras se retorna None.
        """
        return self.shopping[-1] if len(self.shopping) > 0 else None

    def number_product_purchased(self, product):
        """
        Método que devuelve la suma de unidades históricamente compradas 
        de un producto en específico, el cual es ingresado como parámetro.  
        """
        number = 0
        for purchase in self.shopping:
            number += purchase["number"] if purchase["product"] == product else 0
        return number

    def __str__(self):
        return f"Se ah creado al Cliente {self.name}" 