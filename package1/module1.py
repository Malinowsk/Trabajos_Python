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

    def buy(self, product , price ,  number = 1):
        purchase = { "code" : ''.join(random.choices(string.ascii_uppercase + string.digits, k=15)), # Genera una cadena aleatoria de 15 caracteres
                    "product" : product ,
                    "price" : price, 
                    "number" : int(number) , 
                    "date" : datetime.date.today().strftime("%d/%m/%Y") }
        self.shopping.append(purchase)
        return purchase
   
    def get_last_purchase(self):
        return self.shopping[-1] if len(self.shopping) > 0 else None

    def number_product_purchased(self, product):
        number = 0
        for purchase in self.shopping:
            number += purchase["number"] if purchase["product"] == product else 0
        return number

    def __str__(self):
        return f"Se ah creado al Cliente {self.name}" 