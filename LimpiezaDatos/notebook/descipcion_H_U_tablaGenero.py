import pandas as pd

def describir_datos(data_frame_limpio):
    print(f"Número de filas{data_frame_limpio.shape[0]}")
    print(f"Número de columnas{data_frame_limpio.shape[1]} ")
    print(f"Columnas disponibles{list(data_frame_limpio.columns)} ")
    print(f"Estadísticas{data_frame_limpio[["id_gender","name"]].describe()}")
    print(f"Valores cátegoricos{data_frame_limpio["name"].value_counts} ")
