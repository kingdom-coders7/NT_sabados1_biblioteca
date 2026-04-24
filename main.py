import pandas as pd
#from notebook.limpieza_tabla_libros import limpiar_tabla_libros
#from simulacion_HU3_5_tabla_libros import simular_libros
from simulacion_HU3_6_tabla_stand import simular_stands
from notebook.limpieza_tabla_stand import limpiar_tabla_stand

#IMPORTAR DATOS H3_1 TABLAUSUARIOS
#from simulacion_HU3_1TablaUsuarios import simular_usuarios

#IMPORTAR DATOS H3_2 TABLAPRESTAMOS
#from simulacion_HU3_2Tablaprestamos import simular_prestamos


#simulaciones = simular_stands(1)
# print(simulaciones)

#simulacion_libros = simular_libros(300)
#simulaciones_ordenadas = pd.DataFrame(simulacion_libros)
#simulaciones_limpias = limpiar_tabla_libros(simulaciones_ordenadas)
#print(simulaciones_limpias)

#simulacionUsuarios=simular_usuarios(3) 

#simulacionPrestamos=simular_prestamos(3)

#print(simulacionPrestamos) #Ecsribir la simulacion requerida

simulacion_stands = simular_stands(200)
simulaciones_ordenadas = pd.DataFrame(simulacion_stands)
simulaciones_limpias = limpiar_tabla_stand(simulaciones_ordenadas)
print(simulaciones_limpias)

