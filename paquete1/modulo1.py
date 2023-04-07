import datetime
import random
import string

class Client:

    def __init__(self, name, email, age, phone):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
        self.shopping = []

    #version con try
    def comprar(self, producto , cantidad = 1): 
        try:
            compra = { "codigo" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                        "producto" : producto , 
                        "cantidad" : int(cantidad) , # posible captura de error
                        "fecha_de_compra" : datetime.date.today().strftime("%d/%m/%Y") }
            self.shopping.append(compra)
            return compra
        except ValueError as e:
            print(f"\nNo se pudo registrar la compra {producto}. \nRevise que la cantidad ingresada corresponda a un numero entero.\n Error {e.args}")
            return None
        except Exception as e:
            print("Ha ocurrido un error no previsto", type(e).__name__ )
            return None

    """ 
    # version sin try
    def comprar(self, producto , cantidad = 1):

        compra = { "codigo" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                    "producto" : producto , 
                    "cantidad" : int(cantidad) , 
                    "fecha_de_compra" : datetime.date.today().strftime("%d/%m/%Y") }
        self.shopping.append(compra)
        return compra

 
    # version con if
    def comprar(self, producto , cantidad = 1):
        if (type(cantidad)==int):
            compra = { "codigo" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                        "producto" : producto , 
                        "cantidad" : int(cantidad) , 
                        "fecha_de_compra" : datetime.date.today().strftime("%d/%m/%Y") }
            self.shopping.append(compra)
            return compra
        else:
            return None
   """

    def obtener_ult_compra(self):
        return self.shopping[-1] if len(self.shopping) > 0 else None

    def cant_producto_comprados(self, producto):
        cantidad = 0
        for prod in self.shopping:
            cantidad += prod["cantidad"] if prod["producto"] == producto else 0    # ESTO VA DAR ERROR SI NO ME ASEGURO QUE CANTIDAD HAY UN NUMERO
        return cantidad

    def __str__(self):
        # código para generar la representación en cadena del objeto
        return f"Se ah creado al Cliente {self.name}" 



