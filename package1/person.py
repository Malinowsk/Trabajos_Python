class Person:

    def __init__(self, name, email, age, phone):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Se ah creado a la Persona {self.name}" 