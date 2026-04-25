
def describir_stand(data_frame_limpio):
    print(f"numero de filas {data_frame_limpio.shape[0]}")
    print(f"numero de columnas {data_frame_limpio.shape[1]}")
    print(f"columnas disponibles {list(data_frame_limpio.columns)}")
    print(f"estadisticas {data_frame_limpio[["location"]].describe()}")
    print(f"valores categoricos {data_frame_limpio["location"].value_counts()}")