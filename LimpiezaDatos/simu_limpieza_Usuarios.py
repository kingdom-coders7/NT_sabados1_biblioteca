import pandas as pd
import sys #significa que se va a usar el sistema operativo para manejar rutas de archivos
import os #significa que se va a usar el sistema operativo para manejar rutas de archivos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))#



#IMPORTAR DATOS H3_1 TABLAUSUARIOS
from utils.simulacion_HU3_1TablaUsuarios import simular_usuarios



#IMPORTAR FUNCION DE LIMPIEZA
from notebook.limpieza_HU1_1_TablaUsuarios import limpiar_tabla_usuarios


simulacionUsuarios=simular_usuarios(10) 
simulaciones_ordenadasUsuarios=pd.DataFrame(simulacionUsuarios)

print("Datos simulados:")
print(simulaciones_ordenadasUsuarios)

# Aplicar limpieza
simulaciones_limpias = limpiar_tabla_usuarios(simulaciones_ordenadasUsuarios)

print("\nDatos limpios:")
print(simulaciones_limpias)


#describir los datos limpios de la tabla usuarios
from notebook.descripcionDatosHU1_TablaUsusarios import descripcion_datos_tabla_usuarios
descripcion_datos_tabla_usuarios(simulaciones_limpias)
