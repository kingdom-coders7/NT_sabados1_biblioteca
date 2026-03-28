#simulacion de datos de usuarios para la HU3.1  
from datetime import datetime,timedelta #libreria para manejar fechas y hora
#libreria para simular correos aleaotorios

from faker import Faker #libreria para generar datos falsos como nombres, correos, fechas, etc. 

import random #libreria para generar numeros aleatorios
def simular_usuarios(numeroUsuarios):

    #semilla de datos para generar los mismos resultados cada vez que se ejecute el codigo
    listaUsuarios = ["Juan Perez", "Maria Gomez", 
                     "Carlos Sanchez", "Ana Rodriguez", "Luis Fernandez",]
    
    listaCedulas = ["12345678", "87654321", "11223344", "44332211", "55667788"] 
    fechaInicial= datetime.now() - timedelta(days=365*2) #fecha de hace 2 años

    fake = Faker()
    usuarios = []
    for _ in range(numeroUsuarios):
        usuario = {
            "id_users": random.choice(listaCedulas), # Asignar una cédula de la lista
            "name":random.choice(listaUsuarios),
            "last_name": fake.last_name(),
            "movil": fake.phone_number(),
            "email": fake.email(),
            "fecha_registro": fake.date_between(start_date='-2y', end_date='today')
        }
        usuarios.append(usuario)
    return usuarios
# Simular 10 usuarios
usuarios_simulados = simular_usuarios(10)