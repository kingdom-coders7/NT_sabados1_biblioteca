import pandas as pd

def limpiar_tabla_genero(setDatosSucios):
    LimpiezaTablaGenero = setDatosSucios.copy()
    
    # Limpiar columnas que son strings en la tabla género
    columnas_texto = ['name']
    for columna in columnas_texto:
        LimpiezaTablaGenero[columna] = LimpiezaTablaGenero[columna].astype("string").str.strip() # Eliminar espacios en blanco al inicio y al final
        LimpiezaTablaGenero[columna] = LimpiezaTablaGenero[columna].str.lower() # Convertir a minúsculas para estandarizar
    
    # Definir valores esperados para cada columna
    valores_esperados = {
        'id_gender': setDatosSucios['id_gender'].dropna().unique(), # Obtener los valores únicos no nulos de la columna id_gender
        'name': setDatosSucios['name'].dropna().str.title() # Obtener los valores únicos no nulos de la columna name, con la primera letra en mayúscula
    }

    # Reemplazar valores NaN por 000 en la columna id_gender
    LimpiezaTablaGenero['id_gender'] = LimpiezaTablaGenero['id_gender'].fillna(000)

    # Poner la primera letra de cada palabra en mayúsculas y el resto en minúsculas
    LimpiezaTablaGenero['name'] = LimpiezaTablaGenero['name'].str.title()

    # En la columna name donde haya números reemplazar por string "sinAsignar"
    LimpiezaTablaGenero['name'] = LimpiezaTablaGenero['name'].apply(lambda x: x if not any(char.isdigit() for char in str(x)) else 'sinAsignar')
    
    # Evaluar columnas numéricas
    LimpiezaTablaGenero["id_gender"] = pd.to_numeric(LimpiezaTablaGenero["id_gender"],
     errors='coerce') # Convertir a numérico, los valores no convertibles se establecerán como NaN
    
    return LimpiezaTablaGenero
