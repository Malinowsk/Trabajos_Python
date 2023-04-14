import json 
import os
#from google.colab import drive
#drive.mount('/drive/')
path_database = './register_users.json' # ruta de la base de datos

def read_data():
  """
  Función que devuelve un diccionario de todos los datos de la base de datos.
  """
  if os.path.exists(path_database): # consulta si el archivo que simula de bbdd esta creado
    with open(path_database, "r") as file: # en caso true, se lee el archivo json
      return json.load(file) # Se retorna el diccionario con todos los datos
  else:
    return {}  # en caso false, devuelvo un diccionario vacio
  
def save_register(user,password):
  """
  Procedimiento que guarda el registro 
  del usuario y contraseña en la base de datos. 
  """
  data = read_data() # Se leen los datos de la bbdd
  data.update({user : password})
  with open(path_database, 'w') as file:
    json.dump(data, file, indent=4) # Se actualiza la bbdd

def create_register(): 
  """
  Procedimiento que cumple la función de registrar al
  solicitante, con usuario y contraseña en la base de datos. 
  """
  user = input("Ingrese el nombre de usuario: ") # Se pide un usuario
  password = input("Ingrese una contraseña: ") # Se pide una contraseña
  save_register(user,password) # Se guarda el registro

def show_data():
  """
  Procedimiento que muestra la informacion correspondiente 
  a todos los usuarios y contraseñas alojados en la base de datos.
  """
  data = read_data() # Se leen los datos de la bbdd
  print("La información almacenada en la base de datos es:")
  for key in data: # Se recorre todas las claves del diccionario
    print(f"Usuario: {key} , contraseña: {data[key]}")

def login():
  """
   Procedimiento que cumple la función de logeo, pidiendo y 
   corroborando que el usuario y contraseña esten en la base de datos.
   Por último, imprime mensaje si se encuentra logeado
   o de lo contrario hubo inconsistencia en los datos.  
  """
  user = input("Usuario: ")
  data = read_data() # Se leen los datos de la bbdd
  if (user in data):  # Consulta si el usuario ingresado existe en la bbdd
    password = input("Contraseña: ")
    if (data[user] == password): # Consulta si la contraseña ingresada corresponde a la del usuario
      print("Perfecto, usted esta logeado!")
    else:
      print("La contraseña es incorrecta!")
  else:
    print("el usuario no existe!")