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

    def buy(self, product , number = 1):
        purchase = { "code" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                    "product" : product , 
                    "number" : int(number) , 
                    "date" : datetime.date.today().strftime("%d/%m/%Y") }
        self.shopping.append(purchase)
        return purchase
   
    def get_last_purchase(self):
        return self.shopping[-1] if len(self.shopping) > 0 else None

    def number_product_purchased(self, product):
        number = 0
        for purchase in self.shopping:
            number += purchase["number"] if purchase["product"] == product else 0    # ESTO VA DAR ERROR SI NO ME ASEGURO QUE number HAY UN NUMERO
        return number

    def __str__(self):
        # código para generar la representación en cadena del objeto
        return f"Se ah creado al Cliente {self.name}" 

    """ 
    #version con try
    def buy(self, product , number = 1): 
        try:
            purchase = { "code" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                        "product" : product , 
                        "number" : int(number) , # posible captura de error
                        "fecha_de_purchase" : datetime.date.today().strftime("%d/%m/%Y") }
            self.shopping.append(purchase)
            return purchase
        except ValueError as e:
            print(f"\nNo se pudo registrar la purchase {product}. \nRevise que la number ingresada corresponda a un numero entero.\n Error {e.args}")
            return None
        except Exception as e:
            print("Ha ocurrido un error no previsto", type(e).__name__ )
            return None
    
    # version sin try
    def buy(self, product , number = 1):

        purchase = { "code" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                    "product" : product , 
                    "number" : int(number) , 
                    "fecha_de_purchase" : datetime.date.today().strftime("%d/%m/%Y") }
        self.shopping.append(purchase)
        return purchase
    """