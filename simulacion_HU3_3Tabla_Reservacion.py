from datetime import datetime, timedelta
import random

def simular_reserva(numeroReservas):
    
    #Semilla de datos
    listaReserva=["Reserva1","Reserva2","Reserva3","Reserva4","Reserva5"]
    
    listaCodigos=["LIB01R",
                  "LIB02R",
                  "LIB03R",
                  "LIB04R",
                  "LIB05R"]
    
    fechaInicial=datetime(2026,1,1)

    reservas=[]

    for _ in range(numeroReservas):
        fechaSimulada=fechaInicial+timedelta(days=random.randint(0,60))
        reservation={
            "id_reservation":random.randint(0,5000),
            "codigo":random.choice(listaCodigos),
            "id_book":random.randint(0,5000),
            "nombre":random.choice(listaReserva),
            "reservationDate":fechaSimulada.strftime("%Y/%m/%d"),
            "expDate":fechaSimulada.strftime("%Y/%m/%d"),
            "id_employee":random.randint(0,500),
            "id_users":random.randint(0,500)
        }
        reservation.append(reservation)
    return reservation