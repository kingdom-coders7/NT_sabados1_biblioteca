#simulacion de datos para tabla de prestamos para la HU3.2
from datetime import datetime,timedelta #libreria para manejar fechas y horas
from faker import Faker #libreria para generar datos falsos como nombres, correos, fechas, etc. 
import random #libreria para generar numeros aleatorios 

def simular_prestamos(numeroPrestamos):
    fake = Faker()
    prestamos = []
    for _ in range(numeroPrestamos):
        prestamo = {
            "id_prestamo": random.randint(1, 1000),
            "id_users": random.randint(1, 1000), # Asumiendo que los IDs de usuarios van del 1 al 1000
            "id_libro": random.randint(1, 500), # Asumiendo que los IDs de libros van del 1 al 500
            "fecha_prestamo": fake.date_between(start_date='-1y', end_date='today'),
            "fecha_devolucion": fake.date_between(start_date='today', end_date='+30d')
        }

        # Inyectar errores controlados
        probabilidad_error = random.random()
        if probabilidad_error < 0.1:  # 10% de probabilidad de generar un error
            prestamo["id_users"] = None  # ID de usuario no válido
            prestamo["id_libro"] = "invalid"  # ID de libro no válido (cambiar a string inválido)
        elif probabilidad_error < 0.2:  # 20% de probabilidad de generar otro error
            prestamo["fecha_prestamo"] = None  # Fecha de préstamo no válida
        elif probabilidad_error < 0.3:
            prestamo["fecha_devolucion"] = None
            prestamo["id_prestamo"] = random.choice([None, -1, 0])  # ID de préstamo no válido
        elif probabilidad_error < 0.6:
            prestamo["id_libro"] = None 
            prestamo["id_prestamo"] = "texto @ ;"  # ID de préstamo no válido    
        prestamos.append(prestamo)
    return prestamos

#pendiente realizar el pull request para agregar este codigo al repositorio