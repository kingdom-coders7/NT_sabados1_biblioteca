import pandas as pd
import sys #significa que se va a usar el sistema operativo para manejar rutas de archivos
import os #significa que se va a usar el sistema operativo para manejar rutas de archivos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# IMPORTAR DATOS SIMULACION HU3_2 TABLA PRESTAMOS
from utils.simulacion_HU3_2Tablaprestamos import simular_prestamos


# IMPORTAR FUNCION DE LIMPIEZA HU1_2 TABLA PRESTAMOS
from notebook.limpieza_HU1_2_TablaPrestamos import limpiar_tabla_prestamos


simulacionPrestamos=simular_prestamos(5)
simulaciones_ordenadasPrestamos=pd.DataFrame(simulacionPrestamos)
print("Datos simulados:")
print(simulaciones_ordenadasPrestamos)

# Llamar a la función de limpieza
simulaciones_limpiasPrestamos = limpiar_tabla_prestamos(simulaciones_ordenadasPrestamos)


#describir los datos limpios de la tabla prestamos    
from notebook.descripcionDatosHU1_TablaPrestamos import descripcion_datos_tabla_prestamos
descripcion_datos_tabla_prestamos(simulaciones_limpiasPrestamos)

print("Datos limpios:")
print(simulaciones_limpiasPrestamos)
