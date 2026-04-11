import random

def simular_stands(numeroStands):
    
    #Semilla de datos
    listaStands=["EST001", "EST002", "EST003"]

    listaLocacion=["Fundamentos", "Desarrollo Web y Móvil", "Ciencia de Datos y Arquitectura"]


    stands=[]

    for _ in range(numeroStands):
        
        stand={
            "id_stand": random.choice(listaStands),
            "location":random.choice(listaLocacion),
        }
        stands.append(stand)
        return stands