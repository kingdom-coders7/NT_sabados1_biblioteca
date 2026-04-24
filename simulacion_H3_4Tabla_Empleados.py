from datetime import datetime, timedelta
import random

def simular_empleado(numeroEmpleados):
    
    #Semilla de datos
    listaNombres=["Oliver","Seiya","Goku","Kratos","Batman"]

    
    
    fechaInicial=datetime(2026,1,1)

    empleados=[]

    for _ in range(numeroEmpleados):
        fechaSimulada=fechaInicial+timedelta(days=random.randint(0,60))
        employee={
            "id_employee":random.randint(0,5000),
            "name":random.choice(listaNombres),
            
        }
        employee.append(employee)
    return employee
