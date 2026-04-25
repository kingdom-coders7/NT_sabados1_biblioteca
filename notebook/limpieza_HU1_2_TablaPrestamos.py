import pandas as pd

def limpiar_tabla_prestamos(setDatosSucios):
    LimpiezaTablaPrestamos = setDatosSucios.copy()
    
    #Limpiar columnas que son strings en la tabla prestamos
    columnas_texto = ['id_users', 'id_libro', 'fecha_prestamo', 'fecha_devolucion']
    for columna in columnas_texto:
        LimpiezaTablaPrestamos[columna] = LimpiezaTablaPrestamos[columna].astype("string").str.strip() # Eliminar espacios en blanco al inicio y al final
        LimpiezaTablaPrestamos[columna] = LimpiezaTablaPrestamos[columna].str.lower() # Convertir a minúsculas para estandarizar
    
    #Definir valores esperados para cada columna
    valores_esperados = {
        'id_prestamo': setDatosSucios['id_prestamo'].dropna().unique(), # Obtener los valores únicos no nulos de la columna id_prestamo
        'id_users': setDatosSucios['id_users'].dropna().unique(), # Obtener los valores únicos no nulos de la columna id_users
        'id_libro': setDatosSucios['id_libro'].dropna().unique(),
        'nameBook': setDatosSucios['nameBook'].dropna().unique(), # Obtener los valores únicos no nulos de la columna nameBook
        'fecha_prestamo': setDatosSucios['fecha_prestamo'].dropna().unique(), # Obtener los valores únicos no nulos de la columna fecha_prestamo
        'fecha_devolucion': setDatosSucios['fecha_devolucion'].dropna().unique() # Obtener los valores únicos no nulos de la columna fecha_devolucion
    }

    # Reemplazar valores NaN por 000 en la columna id_prestamo
    LimpiezaTablaPrestamos['id_prestamo'] = LimpiezaTablaPrestamos['id_prestamo'].fillna(000)
    
    #evaluar columnas numericas
    LimpiezaTablaPrestamos ["id_prestamo"] = pd.to_numeric(LimpiezaTablaPrestamos ["id_prestamo"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN
    
    LimpiezaTablaPrestamos ["id_users"] = pd.to_numeric(LimpiezaTablaPrestamos ["id_users"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN
    
    LimpiezaTablaPrestamos ["id_libro"] = pd.to_numeric(LimpiezaTablaPrestamos ["id_libro"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN  

#Columna de nameBook, eliminar caracteres especiales y números, dejando solo letras y espacios
    LimpiezaTablaPrestamos['nameBook'] = LimpiezaTablaPrestamos['nameBook'].str.replace(r'[^a-zA-Z\s]', '', regex=True)
    LimpiezaTablaPrestamos['nameBook'] = LimpiezaTablaPrestamos['nameBook'].str.title() # Poner la primera letra de cada palabra en mayúscula y el resto en minúscula


    #Columna de fecha prestamo, convertir a formato de fecha sin hora.
    LimpiezaTablaPrestamos['fecha_prestamo'] = pd.to_datetime(LimpiezaTablaPrestamos['fecha_prestamo'], errors='coerce') # Convertir a formato de fecha, los valores no convertibles se establecerán como NaT (Not a Time)
    
    #Columna de fecha devolucion, convertir a formato de fecha sin hora.
    LimpiezaTablaPrestamos['fecha_devolucion'] = pd.to_datetime(LimpiezaTablaPrestamos['fecha_devolucion'], errors='coerce') # Convertir a formato de fecha, los valores no convertibles se establecerán como NaT (Not a Time)  
   
    #Reemplazar fechas nulas por una fecha por defaulto (por ejemplo, la fecha actual)
    fecha_actual = pd.to_datetime('2026-01-01') # Puedes ajustar esta fecha según tus necesidades
    LimpiezaTablaPrestamos['fecha_prestamo'] = LimpiezaTablaPrestamos['fecha_prestamo'].fillna(fecha_actual)
    LimpiezaTablaPrestamos['fecha_devolucion'] = LimpiezaTablaPrestamos['fecha_devolucion'].fillna(fecha_actual)    
    return LimpiezaTablaPrestamos