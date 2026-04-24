from simulacion_HU3_5_tabla_libros import simular_libros
from simulacion_HU3_6_tabla_stand import simular_stands

#IMPORTAR DATOS H3_1 TABLAUSUARIOS
from simulacion_HU3_1TablaUsuarios import simular_usuarios

#IMPORTAR DATOS H3_2 TABLAPRESTAMOS
from simulacion_HU3_2Tablaprestamos import simular_prestamos





simulaciones = simular_stands(1)
# print(simulaciones)

simulaciones = simular_libros(1)
print(simulaciones)

simulacionUsuarios=simular_usuarios(3) 

simulacionPrestamos=simular_prestamos(3)

print(simulacionPrestamos) #Ecsribir la simulacion requerida
