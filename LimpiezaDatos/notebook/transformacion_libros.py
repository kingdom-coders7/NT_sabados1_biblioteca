import pandas as pd
import matplotlib.pyplot as plt


def transformar_datos(data_frame_limpio):

    # =====================================================
    # 1. Libros con más de 500 páginas
    # =====================================================

    filtro_paginas = data_frame_limpio.query("pages >= 500")

    agrupacion_paginas = (
        filtro_paginas
        .groupby("author")["pages"]
        .count()
        .reset_index(name="cantidad_libros_largos")
        .sort_values(by="cantidad_libros_largos", ascending=False)
    )


    # =====================================================
    # 2. Cantidad de libros por género
    # =====================================================

    agrupacion_generos = (
        data_frame_limpio
        .groupby("id_gender")["id_books"]
        .count()
        .reset_index(name="cantidad_libros")
        .sort_values(by="cantidad_libros", ascending=False)
    )


    # =====================================================
    # 3. Libros organizados por stand
    # =====================================================

    agrupacion_stand = (
        data_frame_limpio
        .groupby("id_stand")["id_books"]
        .count()
        .reset_index(name="cantidad_por_stand")
        .sort_values(by="cantidad_por_stand", ascending=False)
    )


    # =====================================================
    # 4. Editoriales con libros de más de 800 páginas
    # =====================================================

    filtro_editoriales = data_frame_limpio.query("pages >= 800")

    agrupacion_editoriales = (
        filtro_editoriales
        .groupby("editor")["pages"]
        .count()
        .reset_index(name="libros_extensos")
        .sort_values(by="libros_extensos", ascending=False)
    )


    # =====================================================
    # 5. Promedio de páginas por género
    # =====================================================

    agrupacion_promedio_paginas = (
        data_frame_limpio
        .groupby("id_gender")["pages"]
        .mean()
        .reset_index(name="promedio_paginas")
        .sort_values(by="promedio_paginas", ascending=False)
    )


    # =====================================================
    # Resumen general
    # =====================================================

    transformar_resumen = {

        "librosLargosPorAutor": agrupacion_paginas,

        "cantidadLibrosPorGenero": agrupacion_generos,

        "cantidadLibrosPorStand": agrupacion_stand,

        "editorialesLibrosExtensos": agrupacion_editoriales,

        "promedioPaginasPorGenero": agrupacion_promedio_paginas
    }

    return transformar_resumen


def graficar_resultados(resultado):

    # ==========================================
    # 1. Libros largos por autor
    # ==========================================

    grafica1 = resultado["librosLargosPorAutor"]

    plt.figure(figsize=(10,5))
    plt.bar(grafica1["author"], grafica1["cantidad_libros_largos"])
    plt.title("Libros largos por autor")
    plt.xlabel("Autor")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.show()


    # ==========================================
    # 2. Cantidad de libros por género
    # ==========================================

    grafica2 = resultado["cantidadLibrosPorGenero"]

    plt.figure(figsize=(8,5))
    plt.bar(grafica2["id_gender"], grafica2["cantidad_libros"])
    plt.title("Cantidad de libros por género")
    plt.xlabel("Género")
    plt.ylabel("Cantidad")
    plt.show()


    # ==========================================
    # 3. Cantidad de libros por stand
    # ==========================================

    grafica3 = resultado["cantidadLibrosPorStand"]

    plt.figure(figsize=(6,5))
    plt.bar(grafica3["id_stand"], grafica3["cantidad_por_stand"])
    plt.title("Libros por stand")
    plt.xlabel("Stand")
    plt.ylabel("Cantidad")
    plt.show()


    # ==========================================
    # 4. Editoriales con libros extensos
    # ==========================================

    grafica4 = resultado["editorialesLibrosExtensos"]

    plt.figure(figsize=(10,5))
    plt.bar(grafica4["editor"], grafica4["libros_extensos"])
    plt.title("Editoriales con libros extensos")
    plt.xlabel("Editorial")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.show()


    # ==========================================
    # 5. Promedio páginas por género
    # ==========================================

    grafica5 = resultado["promedioPaginasPorGenero"]

    plt.figure(figsize=(8,5))
    plt.bar(grafica5["id_gender"], grafica5["promedio_paginas"])
    plt.title("Promedio de páginas por género")
    plt.xlabel("Género")
    plt.ylabel("Promedio")
    plt.show()

    