import pandas as pd

def limpiar_tabla_libros(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #1. Limpiar las columnas del dataframe que son palabras (strings)
    columnas_texto = ["id_books", "title", "author", "editor"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    #2. Definir valores esperados
    autores_validos = ["Brian W.", "Luis Joyanes Aguilar", "Ricardo W.", "Hadley Wickham", "Jesús Ormaza"]
    data_frame_limpio["author"] = data_frame_limpio["author"].where(
        data_frame_limpio["author"].isin(autores_validos),
        pd.NA
    )

    editorial_valida = ["O’Reilly Media", "Packt Publishing", "Apress (Springer)", "McGraw-Hill Education", "Anaya Multimedia"]
    data_frame_limpio["editor"] = data_frame_limpio["editor"].where(
        data_frame_limpio["editor"].isin(editorial_valida),
        pd.NA
    )

    id_valida = ["SBN123", "SBN001", "SBN423", "SBN879", "SBN400"]
    data_frame_limpio["id_books"] = data_frame_limpio["id_books"].where(
        data_frame_limpio["id_books"].isin(id_valida),
        pd.NA
    )

    libros_validos = ["Codigo limpio", "Fundamentos de programación en C#", "Python 3", "Javascript en un fin de semana", "C++ practico"]
    data_frame_limpio["title"] = data_frame_limpio["title"].where(
        data_frame_limpio["title"].isin(libros_validos),
        pd.NA
    )

    #3. Evaluar columnas numericas
    data_frame_limpio["pages"] = pd.to_numeric(data_frame_limpio["pages"])
    data_frame_limpio["id_gender"] = pd.to_numeric(data_frame_limpio["id_gender"])
    data_frame_limpio["id_stand"] = pd.to_numeric(data_frame_limpio["id_stand"])

    #4. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias = ["id_books", "title", "author", "editor", "pages", "id_stand", "id_gender"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    #5. Eliminar valores duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio