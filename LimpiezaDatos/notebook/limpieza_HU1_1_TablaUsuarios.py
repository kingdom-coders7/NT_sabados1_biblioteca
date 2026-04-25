import pandas as pd

def limpiar_tabla_usuarios(setDatosSucios):
    LimpiezaTablaUsuarios = setDatosSucios.copy()
    
    #Limpiar columnnas que son strings en la tabla usuarios
    columnas_texto = ['name', 'last_name', 'email', 'movil']
    for columna in columnas_texto:
        LimpiezaTablaUsuarios[columna] = LimpiezaTablaUsuarios[columna].astype("string").str.strip() # Eliminar espacios en blanco al inicio y al final
        LimpiezaTablaUsuarios[columna] = LimpiezaTablaUsuarios[columna].str.lower() # Convertir a minúsculas para estandarizar
    
    #Definir valores esperados para cada columna
    valores_esperados = {
        'id_users': setDatosSucios['id_users'].dropna().unique(), # Obtener los valores únicos no nulos de la columna id_users
        'name': setDatosSucios['name'].dropna().str.title(),# Obtener los valores únicos no nulos de la columna name, con la primera letra en mayúscula
        'last_name': setDatosSucios['last_name'].dropna().str.title(), # Obtener los valores únicos no nulos de la columna last_name, con la primera letra en mayúscula
        'email': setDatosSucios['email'].dropna().unique(),
        'movil': setDatosSucios['movil'].dropna().unique(),
        'fecha_registro': setDatosSucios['fecha_registro'].dropna().unique()
    }

# Reemplazar valores NaN por 000 en la columna id_users
    LimpiezaTablaUsuarios['id_users'] = LimpiezaTablaUsuarios['id_users'].fillna(000)

    # Poner la primera letra de cada palabra en mayúsculas y el resto en minúsculas
    LimpiezaTablaUsuarios['name'] = LimpiezaTablaUsuarios['name'].str.title()
    LimpiezaTablaUsuarios['last_name'] = LimpiezaTablaUsuarios['last_name'].str.title()

    #en la columna name donde haya numeros reemplazar por string "sinAsignar"
    LimpiezaTablaUsuarios['name'] = LimpiezaTablaUsuarios['name'].apply(lambda x: x if not any(char.isdigit() for char in str(x)) else 'sinAsignar')
    
    #evaluar columnas numericas
    LimpiezaTablaUsuarios ["id_users"] = pd.to_numeric(LimpiezaTablaUsuarios ["id_users"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN
    

    #corregir columna de email con @por defecto
    LimpiezaTablaUsuarios['email'] = LimpiezaTablaUsuarios['email'].apply(lambda x: x if '@' in str(x) else 'correo_invalido')

    #Colmna de fecha registro, convertir a formato de fecha sin hora.

    LimpiezaTablaUsuarios['fecha_registro'] = pd.to_datetime(LimpiezaTablaUsuarios['fecha_registro'], errors='coerce') # Convertir a formato de fecha, los valores no convertibles se establecerán como NaT (Not a Time)
   
   #Reemplazar fechas nulas por una fecha por defaulto (por ejemplo, la fecha actual)
    fecha_actual = pd.to_datetime('2026-01-01') # Puedes ajustar esta fecha según tus necesidades
    LimpiezaTablaUsuarios['fecha_registro'] = LimpiezaTablaUsuarios['fecha_registro'].fillna(fecha_actual)
    return LimpiezaTablaUsuarios 