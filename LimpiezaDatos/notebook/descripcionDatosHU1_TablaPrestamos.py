import pandas as pd

def descripcion_datos_tabla_prestamos(limpiezaTablaPrestamos):
    print(f"numero de filas: {limpiezaTablaPrestamos.shape[0]}")
    print(f"numero de columnas: {limpiezaTablaPrestamos.shape[1]}")
    print(f"columnas disponibles: {list(limpiezaTablaPrestamos.columns)}")
    print(f"estadisticas): {limpiezaTablaPrestamos[['id_prestamo', 'id_users','id_libro']].count()}")
    print(f"valores categoricos: {limpiezaTablaPrestamos['id_prestamo'].value_counts()}")
    print(f"fecha minima: {limpiezaTablaPrestamos['fecha_prestamo'].min()}")
    print(f"fecha maxima: {limpiezaTablaPrestamos['fecha_prestamo'].max()}")
    print(f"fecha minima: {limpiezaTablaPrestamos['fecha_devolucion'].min()}")
    print(f"fecha maxima: {limpiezaTablaPrestamos['fecha_devolucion'].max()}")
    print(f"libros mas prestados: {limpiezaTablaPrestamos['nameBook'].value_counts().head(5)}")
    print(f"usuarios con mas prestamos: {limpiezaTablaPrestamos['id_users'].value_counts().head(5)}")   
    print(f"tiempo promedio de prestamo: {(limpiezaTablaPrestamos['fecha_devolucion'] - limpiezaTablaPrestamos['fecha_prestamo']).mean()}   ")