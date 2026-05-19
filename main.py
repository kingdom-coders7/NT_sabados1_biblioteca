import pandas as pd
#from LimpiezaDatos.notebook.transformacion_libros import transformar_datos, graficar_resultados
from LimpiezaDatos.notebook.transformacion_stand import transformar_datos_stand, graficar_resultados
#from LimpiezaDatos.notebook.limpieza_tabla_libros import limpiar_tabla_libros
#from utils.simulacion_HU3_5_tabla_libros import simular_libros
#from utils.simulacion_HU3_6_tabla_stand import simular_stands
#from LimpiezaDatos.notebook.limpieza_tabla_stand import limpiar_tabla_stand
#from utils.simulacion_H3_4Tabla_Genero import simular_Gender
#from LimpiezaDatos.notebook.limpieza_H_U_TablaGenero import limpiar_tabla_genero
#from LimpiezaDatos.notebook.limpiezaH_U_TablaReservaciones import limpiar_tabla_reservaciones
#from utils.simulacion_HU3_3Tabla_Reservacion import simular_reserva
from utils.simulacion_H3_4Tabla_Genero import simular_Gender
from LimpiezaDatos.notebook.limpieza_H_U_TablaGenero import limpiar_tabla_genero





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


#simulaciones = simular_stands(30)
#print(simulaciones)

#simulacionPrestamos=simular_prestamos(3)

#print(simulacionPrestamos) #Ecsribir la simulacion requerida

#simulacion_stands = simular_stands(200)
#simulaciones_ordenadas = pd.DataFrame(simulacion_stands)
#simulaciones_limpias = limpiar_tabla_stand(simulaciones_ordenadas)
#print(simulaciones_limpias)

#simulacion reservas
#simular_reserva = simular_reserva(25)
#print(simular_reserva)

#reserva limpia
#simulacion_reserva = simular_reserva(25)
#simulaciones_ordenadas = pd.DataFrame(simulacion_reserva)
#simulaciones_limpias = limpiar_tabla_reservaciones(simulaciones_ordenadas)
#print(simulaciones_limpias)

#gender_simulado = simular_Gender(30)
#print(gender_simulado)

#simular_genero = simular_Gender(30)
#simulaciones_ordenadas = pd.DataFrame(simular_genero)
#simulaciones_limpias = limpiar_tabla_genero(simulaciones_ordenadas)
#print(simulaciones_limpias)

#importar descripcion de libros
#from LimpiezaDatos.notebook.descripcion_tabla_libros import describir_libros  # noqa: E402

#describir_libros(simulaciones_limpias)

#importacion descripcion stands
#from notebook.descripcion_tabla_stand import describir_stand # noqa: E402

#describir_stand(simulaciones_limpias)

#importacion descripcion genero
#from LimpiezaDatos.notebook.descipcion_H_U_tablaGenero import describir_datos  # noqa: E402

#describir_datos(simulaciones_limpias)

#importacion descripción reservas
#from LimpiezaDatos.notebook.descripcion_H_U_tablaReservacion import describir_reserva # noqa: E402

#describir_reserva(simulaciones_limpias)

#df = pd.read_csv("books.csv")


# =========================================
# TRANSFORMAR
# =========================================

#resultado = transformar_datos(df)


# =========================================
# MOSTRAR RESULTADOS
# =========================================

#print(resultado["cantidadLibrosPorGenero"])

#print(resultado["cantidadLibrosPorStand"])


# =========================================
# GRAFICAR
# =========================================

#graficar_resultados(resultado)

# =========================================
# EXTRAER CSV
# =========================================

df = pd.read_csv("stands.csv")




# =========================================
# TRANSFORMAR
# =========================================

resultado = transformar_datos_stand(df)


# =========================================
# MOSTRAR RESULTADOS
# =========================================

print(resultado["cantidadPorStand"])

print(resultado["cantidadPorUbicacion"])


# =========================================
# GRAFICAR
# =========================================

graficar_resultados(resultado)

