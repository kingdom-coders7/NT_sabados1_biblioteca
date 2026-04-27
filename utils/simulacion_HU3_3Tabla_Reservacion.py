from datetime import datetime, timedelta
import random

def simular_reserva(numeroReservas):
    
    #Semilla de datos
    listaReserva=["reserva1","reserva2","reserva3","reserva4","reserva5"]
    
    listaCodigos=["lib01",
                  "lib02",
                  "lib03",
                  "lib04",
                  "lib05"]
    
    listaGeneros=["Literatura","Terror","Ficción","Historia","Novelas"]

  

    
    fechaInicial=datetime(2026,1,1)

    reservas=[]

    for _ in range(numeroReservas):
        fechaSimulada=fechaInicial+timedelta(days=random.randint(0,60))
        reservation={
            "id_reservation":random.choice(listaReserva),
            "codigo":random.choice(listaCodigos),
            "id_book":random.randint(0,500),
            "reservationDate":fechaSimulada.strftime("%Y/%m/%d"),
            "expDate":fechaSimulada.strftime("%Y/%m/%d"),
            "id_gender":random.choice(listaGeneros),
            "id_users":random.randint(0,500)
        }
        
        # Inyectar errores controlados
        probabilidad_error = random.random()
        if probabilidad_error < 0.1:  
            reservation["id_reservation"] = None 
            reservation["id_book"] = None  
        elif probabilidad_error < 0.2:  
            reservation["nombre"] = None  
        elif probabilidad_error < 0.3:
            reservation["reservationDate"] = None
            reservation["id_users"] = random.choice([None, -1, 0]) 
        elif probabilidad_error < 0.6:
            reservation["id_gender"] = "Error404"
            reservation["expDate"] = "texto 1@1 ;"  
            reservation["codigo"] = "Bad gate"
  
        reservas.append(reservation)
    return reservas