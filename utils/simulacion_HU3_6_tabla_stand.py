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

        #Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.25:
            stand["id_stand"] = None
        elif probabilidadError < 0.5:
            stand["location"] = random.choice(["La cocina", "carniceria"])
        stands.append(stand)
        
    return stands