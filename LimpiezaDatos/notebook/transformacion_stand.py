import pandas as pd
import matplotlib.pyplot as plt


def transformar_datos_stand(data_frame_limpio):

    # =====================================================
    # 1. Cantidad de registros por stand
    # =====================================================

    agrupacion_stand = (
        data_frame_limpio
        .groupby("id_stand")["location"]
        .count()
        .reset_index(name="cantidad_registros")
        .sort_values(by="cantidad_registros", ascending=False)
    )


    # =====================================================
    # 2. Cantidad de registros por ubicación
    # =====================================================

    agrupacion_location = (
        data_frame_limpio
        .groupby("location")["id_stand"]
        .count()
        .reset_index(name="cantidad_ubicaciones")
        .sort_values(by="cantidad_ubicaciones", ascending=False)
    )


    # =====================================================
    # 3. Registros del stand EST001
    # =====================================================

    filtro_est001 = (
        data_frame_limpio
        .query("id_stand == 'EST001'")
    )

    agrupacion_est001 = (
        filtro_est001
        .groupby("location")["id_stand"]
        .count()
        .reset_index(name="cantidad_est001")
        .sort_values(by="cantidad_est001", ascending=False)
    )


    # =====================================================
    # 4. Registros en Ciencia de Datos y Arquitectura
    # =====================================================

    filtro_ciencia = (
        data_frame_limpio
        .query("location == 'CIENCIA DE DATOS Y ARQUITECTURA'")
    )

    agrupacion_ciencia = (
        filtro_ciencia
        .groupby("id_stand")["location"]
        .count()
        .reset_index(name="cantidad_ciencia")
        .sort_values(by="cantidad_ciencia", ascending=False)
    )


    # =====================================================
    # 5. Cruce entre stand y ubicación
    # =====================================================

    agrupacion_general = (
        data_frame_limpio
        .groupby(["id_stand", "location"])
        .size()
        .reset_index(name="cantidad")
        .sort_values(by="cantidad", ascending=False)
    )


    # =====================================================
    # RESUMEN GENERAL
    # =====================================================

    transformar_resumen = {

        "cantidadPorStand": agrupacion_stand,

        "cantidadPorUbicacion": agrupacion_location,

        "ubicacionesEst001": agrupacion_est001,

        "standsCienciaDatos": agrupacion_ciencia,

        "cruceStandUbicacion": agrupacion_general
    }

    return transformar_resumen


def graficar_resultados(resultado):

    # ==========================================
    # 1. Cantidad por stand
    # ==========================================

    grafica1 = resultado["cantidadPorStand"]

    plt.figure(figsize=(8,5))

    plt.bar(
        grafica1["id_stand"],
        grafica1["cantidad_registros"]
    )

    plt.title("Cantidad de registros por Stand")
    plt.xlabel("Stand")
    plt.ylabel("Cantidad")

    plt.show()


    # ==========================================
    # 2. Cantidad por ubicación
    # ==========================================

    grafica2 = resultado["cantidadPorUbicacion"]

    plt.figure(figsize=(10,5))

    plt.bar(
        grafica2["location"],
        grafica2["cantidad_ubicaciones"]
    )

    plt.title("Cantidad por ubicación")
    plt.xlabel("Ubicación")
    plt.ylabel("Cantidad")

    plt.xticks(rotation=15)

    plt.show()


    # ==========================================
    # 3. Ubicaciones del stand EST001
    # ==========================================

    grafica3 = resultado["ubicacionesEst001"]

    plt.figure(figsize=(8,5))

    plt.bar(
        grafica3["location"],
        grafica3["cantidad_est001"]
    )

    plt.title("Ubicaciones del Stand EST001")
    plt.xlabel("Ubicación")
    plt.ylabel("Cantidad")

    plt.xticks(rotation=15)

    plt.show()


    # ==========================================
    # 4. Stands en Ciencia de Datos
    # ==========================================

    grafica4 = resultado["standsCienciaDatos"]

    plt.figure(figsize=(8,5))

    plt.bar(
        grafica4["id_stand"],
        grafica4["cantidad_ciencia"]
    )

    plt.title("Stands en Ciencia de Datos")
    plt.xlabel("Stand")
    plt.ylabel("Cantidad")

    plt.show()


    # ==========================================
    # 5. Cruce Stand vs Ubicación
    # ==========================================

    grafica5 = resultado["cruceStandUbicacion"]

    etiquetas = (
        grafica5["id_stand"] +
        " - " +
        grafica5["location"]
    )

    plt.figure(figsize=(12,5))

    plt.bar(
        etiquetas,
        grafica5["cantidad"]
    )

    plt.title("Cruce Stand vs Ubicación")
    plt.xlabel("Stand y Ubicación")
    plt.ylabel("Cantidad")

    plt.xticks(rotation=45)

    plt.show()