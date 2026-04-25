import pandas as pd

def limpiar_tabla_genero(setDatosSucios):
    LimpiezaTablaGenero = setDatosSucios.copy()
    
    # Limpiar columnas que son strings en la tabla género
    columnas_texto = ["id_gender", "name"]
    for columna in columnas_texto:
        LimpiezaTablaGenero[columna] = LimpiezaTablaGenero[columna].astype("string").str.strip() # Eliminar espacios en blanco al inicio y al final
        
    valores_esperados = ["literatura","terror","ficción","historia","novelas"]
    LimpiezaTablaGenero["id_gender"] = LimpiezaTablaGenero["id_gender"].where(
        LimpiezaTablaGenero["id_gender"].isin(valores_esperados),
        pd.NA
    )

    indicador_esperado = ["av", "tr", "fc", "dr"]
    LimpiezaTablaGenero["name"] = LimpiezaTablaGenero["name"].where(
        LimpiezaTablaGenero["name"].isin(indicador_esperado),
        pd.NA
    )


     #4. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias = ["id_gender", "name"]
    LimpiezaTablaGenero = LimpiezaTablaGenero.dropna(subset=columnas_obligatorias)

    LimpiezaTablaGenero = LimpiezaTablaGenero.drop_duplicates()
    
   
    
    return LimpiezaTablaGenero
