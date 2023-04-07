import json 
import os
#from google.colab import drive
#drive.mount('/drive/')
ruta_basededatos = './registro_usuarios.json' # ruta de la base de datos

def leer_datos():
  """
  Función que devuelve un diccionario de todos los datos de la base de datos.
  """
  if os.path.exists(ruta_basededatos): # consulta si el archivo que simula de bbdd esta creado
    with open(ruta_basededatos, "r") as file: # en caso true, se lee el archivo json
      return json.load(file) # Se retorna el diccionario con todos los datos
  else:
    return {}  # en caso false, devuelvo un diccionario vacio
  
def guardar_registro(usuario,contrasenia):
  """
  Procedimiento que guarda el registro 
  del usuario y contraseña en la base de datos. 
  """
  datos = leer_datos() # Se leen los datos de la bbdd
  datos.update({usuario : contrasenia})
  with open(ruta_basededatos, 'w') as file:
    json.dump(datos, file, indent=4) # Se actualiza la bbdd

def crear_registro():
  """
  Procedimiento que cumple la función de registrar al
  solicitante, con usuario y contraseña en la base de datos. 
  """
  usuario = input("Ingrese el nombre de usuario: ") # Se pide un usuario
  contrasenia = input("Ingrese una contraseña: ") # Se pide una contraseña
  guardar_registro(usuario,contrasenia) # Se guarda el registro

def mostrar_datos():
  """
  Procedimiento que muestra la informacion correspondiente 
  a todos los usuarios y contraseñas alojados en la base de datos.
  """
  datos = leer_datos() # Se leen los datos de la bbdd
  print("La información almacenada en la base de datos es:")
  for clave in datos: # Se recorre todas las claves del diccionario
    print(f"Usuario: {clave} , contraseña: {datos[clave]}")

def login():
  """
   Procedimiento que cumple la función de logeo, pidiendo y 
   corroborando que el usuario y contraseña esten en la base de datos.
   Por último, imprime mensaje si se encuentra logeado
   o de lo contrario hubo inconsistencia en los datos.  
  """
  usuario = input("Usuario: ")
  datos = leer_datos() # Se leen los datos de la bbdd
  if (usuario in datos):  # Consulta si el usuario ingresado existe en la bbdd
    contrasenia = input("Contraseña: ")
    if (datos[usuario] == contrasenia): # Consulta si la contraseña ingresada corresponde a la del usuario
      print("Perfecto, usted esta logeado!")
    else:
      print("La contraseña es incorrecta!")
  else:
    print("el usuario no existe!")


"""
crear_registro() # Se crea un registro

mostrar_datos() # Se imprime todos los datos de los usuarios

login() # Ejecución del procedimiento de logeo
"""