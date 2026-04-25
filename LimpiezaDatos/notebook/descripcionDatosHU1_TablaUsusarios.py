import pandas as pd

def descripcion_datos_tabla_usuarios(limpiezaTablaUsuarios):
     print(f"numero de filas: {limpiezaTablaUsuarios.shape[0]}")
     print(f"numero de columnas: {limpiezaTablaUsuarios.shape[1]}")
     print(f"columnas disponibles: {list(limpiezaTablaUsuarios.columns)}")
     print(f"estadisticas): {limpiezaTablaUsuarios[['name', 'last_name','ciudad']].count()}")
     print(f"valores categoricos: {limpiezaTablaUsuarios['ciudad'].value_counts()}")
     print(f"fecha minima: {limpiezaTablaUsuarios['fecha_registro'].min()}")
     print(f"fecha maxima: {limpiezaTablaUsuarios['fecha_registro'].max()}")
     print(f"numero de usuarios registrados por mes: {limpiezaTablaUsuarios['fecha_registro'].dt.month.value_counts()}   ")
     print(f"cantidad de usuarios con email valido: {limpiezaTablaUsuarios[limpiezaTablaUsuarios['email'] != 'correo_invalido'].shape[0]}       ")
     print(f"cantidad de usuarios por ciudad: {limpiezaTablaUsuarios['ciudad'].value_counts()} ")