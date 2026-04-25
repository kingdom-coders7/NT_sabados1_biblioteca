import pandas as pd

def limpiar_tabla_reservaciones(setDatosSucios):
    LimpiezaTablaReservaciones = setDatosSucios.copy()
    
    # Limpiar columnas que son strings en la tabla reservaciones
    columnas_texto = ['id_reservation','id_gender',"codigo"]
    for columna in columnas_texto:
        LimpiezaTablaReservaciones[columna] = LimpiezaTablaReservaciones[columna].astype("string").str.strip() # Eliminar espacios en blanco al inicio y al final
        
    # Definir valores esperados para cada columna
    reserva_esperada = ["reserva1","reserva2","reserva3","reserva4","reserva5"]
    LimpiezaTablaReservaciones = ["id_reservation"] = LimpiezaTablaReservaciones["id_reservation"].where(
        LimpiezaTablaReservaciones["id_reservation"].isin(reserva_esperada),
        pd.NA

    )

    genero_esperado = ["literatura","terror","ficción","historia","novelas"]
    LimpiezaTablaReservaciones = ["id_gender"] = LimpiezaTablaReservaciones["id_gender"].where(
        LimpiezaTablaReservaciones["id_gender"].isin(genero_esperado),
        pd.NA

    )

    codigo_esperado = ["lib01","lib02","lib03","lib04","lib05"]
    LimpiezaTablaReservaciones = ["codigo"] = LimpiezaTablaReservaciones["codigo"].where(
        LimpiezaTablaReservaciones["codigo"].isin(codigo_esperado),
        pd.NA

    )

    LimpiezaTablaReservaciones["id_book"] = pd.to_numeric(LimpiezaTablaReservaciones["id_book"])
    LimpiezaTablaReservaciones["id_users"] = pd.to_numeric(LimpiezaTablaReservaciones["id_users"])

        
    # Reemplazar fechas nulas por una fecha por defecto (por ejemplo, la fecha actual)
    fecha_actual = pd.to_datetime('2026-01-01') # Puedes ajustar esta fecha según tus necesidades
    LimpiezaTablaReservaciones['reservationDate'] = LimpiezaTablaReservaciones['reservationDate'].fillna(fecha_actual)
    LimpiezaTablaReservaciones['expDate'] = LimpiezaTablaReservaciones['expDate'].fillna(fecha_actual)

    #Eliminar valores númericos 
    columnas_obligatorias = ["id_reservation","codigo","id_book","reservationDate","expDate","id_gender","id_users"]
    LimpiezaTablaReservaciones = LimpiezaTablaReservaciones.dropna(subset=columnas_obligatorias)

    #Eliminar valores duplicados
    LimpiezaTablaReservaciones=LimpiezaTablaReservaciones.drop_duplicates()
    
    return LimpiezaTablaReservaciones
