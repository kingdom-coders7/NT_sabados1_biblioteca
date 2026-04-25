from datetime import datetime, timedelta
import random

def simular_Gender(numeroGeneros):
    
    #Semilla de datos
    listaGender=["Literatura","Terror","Ficción","Historia","Novelas"]

    
    
    fechaInicial=datetime(2026,1,1)

    gender=[]

    for _ in range(numeroGeneros):
        fechaSimulada=fechaInicial+timedelta(days=random.randint(0,60))
        employee={
            "id_gender":random.randint(0,5000),
            "name":random.choice(listaGender),
            
        }
        gender.append(gender)
    return gender
