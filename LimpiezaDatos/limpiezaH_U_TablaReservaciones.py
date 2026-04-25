import pandas as pd

def limpiar_tabla_reservaciones(setDatosSucios):
    LimpiezaTablaReservaciones = setDatosSucios.copy()
    
    # Limpiar columnas que son strings en la tabla reservaciones
    columnas_texto = ['codigo', 'nombre']
    for columna in columnas_texto:
        LimpiezaTablaReservaciones[columna] = LimpiezaTablaReservaciones[columna].astype("string").str.strip() # Eliminar espacios en blanco al inicio y al final
        LimpiezaTablaReservaciones[columna] = LimpiezaTablaReservaciones[columna].str.lower() # Convertir a minúsculas para estandarizar
    
    # Definir valores esperados para cada columna
    valores_esperados = {
        'id_reservation': setDatosSucios['id_reservation'].dropna().unique(), # Obtener los valores únicos no nulos de la columna id_reservation
        'codigo': setDatosSucios['codigo'].dropna().unique(), # Obtener los valores únicos no nulos de la columna codigo
        'id_book': setDatosSucios['id_book'].dropna().unique(), # Obtener los valores únicos no nulos de la columna id_book
        'nombre': setDatosSucios['nombre'].dropna().str.title(), # Obtener los valores únicos no nulos de la columna nombre, con la primera letra en mayúscula
        'reservationDate': setDatosSucios['reservationDate'].dropna().unique(), # Obtener los valores únicos no nulos de la columna reservationDate
        'expDate': setDatosSucios['expDate'].dropna().unique(), # Obtener los valores únicos no nulos de la columna expDate
        'id_employee': setDatosSucios['id_employee'].dropna().unique(), # Obtener los valores únicos no nulos de la columna id_employee
        'id_users': setDatosSucios['id_users'].dropna().unique() # Obtener los valores únicos no nulos de la columna id_users
    }

    # Reemplazar valores NaN por 000 en las columnas numéricas principales
    LimpiezaTablaReservaciones['id_reservation'] = LimpiezaTablaReservaciones['id_reservation'].fillna(000)

    # Poner la primera letra de cada palabra en mayúsculas y el resto en minúsculas
    LimpiezaTablaReservaciones['nombre'] = LimpiezaTablaReservaciones['nombre'].str.title()

    # En la columna nombre donde haya números reemplazar por string "sinAsignar"
    LimpiezaTablaReservaciones['nombre'] = LimpiezaTablaReservaciones['nombre'].apply(lambda x: x if not any(char.isdigit() for char in str(x)) else 'sinAsignar')
    
    # Evaluar columnas numéricas
    LimpiezaTablaReservaciones["id_reservation"] = pd.to_numeric(LimpiezaTablaReservaciones["id_reservation"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN
    
    LimpiezaTablaReservaciones["id_book"] = pd.to_numeric(LimpiezaTablaReservaciones["id_book"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN
    
    LimpiezaTablaReservaciones["id_employee"] = pd.to_numeric(LimpiezaTablaReservaciones["id_employee"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN
    
    LimpiezaTablaReservaciones["id_users"] = pd.to_numeric(LimpiezaTablaReservaciones["id_users"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN

    # Columna de reservationDate, convertir a formato de fecha sin hora.
    LimpiezaTablaReservaciones['reservationDate'] = pd.to_datetime(LimpiezaTablaReservaciones['reservationDate'], errors='coerce') # Convertir a formato de fecha, los valores no convertibles se establecerán como NaT (Not a Time)
    
    # Columna de expDate, convertir a formato de fecha sin hora.
    LimpiezaTablaReservaciones['expDate'] = pd.to_datetime(LimpiezaTablaReservaciones['expDate'], errors='coerce') # Convertir a formato de fecha, los valores no convertibles se establecerán como NaT (Not a Time)
   
    # Reemplazar fechas nulas por una fecha por defecto (por ejemplo, la fecha actual)
    fecha_actual = pd.to_datetime('2026-01-01') # Puedes ajustar esta fecha según tus necesidades
    LimpiezaTablaReservaciones['reservationDate'] = LimpiezaTablaReservaciones['reservationDate'].fillna(fecha_actual)
    LimpiezaTablaReservaciones['expDate'] = LimpiezaTablaReservaciones['expDate'].fillna(fecha_actual)
    
    return LimpiezaTablaReservaciones
