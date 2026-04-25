import pandas as pd

def limpiar_tabla_stand(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #1. Limpiar las columnas del dataframe que son palabras (strings)
    columnas_texto = ["id_stand", "location"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    #2. Definir valores esperados
    stands_validos = ["EST001", "EST002", "EST003"]
    data_frame_limpio["id_stand"] = data_frame_limpio["id_stand"].where(
        data_frame_limpio["id_stand"].isin(stands_validos),
        pd.NA
    )

    ubicacion_valida = ["Fundamentos", "Desarrollo Web y Móvil", "Ciencia de Datos y Arquitectura"]
    data_frame_limpio["location"] = data_frame_limpio["location"].where(
        data_frame_limpio["location"].isin(ubicacion_valida),
        pd.NA
    )


    #4. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias = ["id_stand", "location"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    #5. Eliminar valores duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio

