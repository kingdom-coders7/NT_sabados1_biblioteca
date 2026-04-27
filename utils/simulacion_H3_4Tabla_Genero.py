import random

def simular_Gender(numeroGeneros):
    
    #Semilla de datos
    listaId=["lt", "tr", "fc", "dr", "nv"]
    listaGender=["Literatura","Terror","Ficción","Historia","Novelas"]

    

    genders=[]

    for _ in range(numeroGeneros):
        gender={
            "id_gender":random.choice(listaId),
            "name":random.choice(listaGender),    
        }

        #Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.25:
            gender["id_gender"] = None
        elif probabilidadError < 0.3:
            gender["name"] = random.choice(["Peliculas", "Caballos"])
        genders.append(gender)
    
    return genders
