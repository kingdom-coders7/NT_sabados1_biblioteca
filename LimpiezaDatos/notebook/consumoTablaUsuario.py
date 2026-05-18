import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from faker import Faker, Faker
import random

# ──────────────────────────────────────────────
# 1. GENERACIÓN DEL DATASET
# ──────────────────────────────────────────────
def generar_dataset(numeroUsuarios=500):
    fake = Faker("es_CO")
    dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    planes = ["básico", "estándar", "premium", "empresarial"]
    ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
                "Bucaramanga", "Pereira", "Manizales", "Cúcuta", "Ibagué"]

    usuarios = []
    for _ in range(numeroUsuarios):
        fecha_registro = fake.date_between(start_date="-2y", end_date="today")
        usuario = {
            "id_users":        fake.unique.random_number(digits=8),
            "name":            fake.first_name(),
            "last_name":       fake.last_name(),
            "movil":           fake.phone_number(),
            "email":           fake.email(),
            "fecha_registro":  fecha_registro,
            # Columnas enriquecidas para análisis
            "ciudad":          random.choice(ciudades),
            "plan":            random.choice(planes),
            "activo":          random.choice([True, False]),
            "sesiones_mes":    random.randint(0, 120),
            "gasto_total":     round(random.uniform(0, 2_000_000), 2),
            "mes_registro":    fecha_registro.strftime("%Y-%m"),
            "año_registro":    fecha_registro.year,
        }
        usuarios.append(usuario)

    df = pd.DataFrame(usuarios)
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])
    return df


# ──────────────────────────────────────────────
# 2. TRANSFORMACIONES  (formato solicitado)
# ──────────────────────────────────────────────
def transformar_datos(data_frame_limpio: pd.DataFrame) -> dict:

    # FILTRO 1 — Usuarios del plan "premium" → conteo por ciudad
    filtro1 = data_frame_limpio.query("plan == 'premium'")
    agrupacion1 = (
        filtro1.groupby("ciudad")["id_users"]
        .count()
        .reset_index(name="conteo_premium")
        .sort_values("conteo_premium", ascending=False)
    )

    # FILTRO 2 — Usuarios activos → gasto total promedio por plan
    filtro2 = data_frame_limpio.query("activo == True")
    agrupacion2 = (
        filtro2.groupby("plan")["gasto_total"]
        .mean()
        .reset_index(name="gasto_promedio")
        .sort_values("gasto_promedio", ascending=False)
    )

    # FILTRO 3 — Alto consumo (sesiones_mes > 60) → conteo de usuarios por mes
    filtro3 = data_frame_limpio.query("sesiones_mes > 60")
    agrupacion3 = (
        filtro3.groupby("mes_registro")["id_users"]
        .count()
        .reset_index(name="usuarios_activos")
        .sort_values("mes_registro")
    )

    # FILTRO 4 — Gasto >= 500 000 → sumatoria de gasto por ciudad
    filtro4 = data_frame_limpio.query("gasto_total >= 500_000")
    agrupacion4 = (
        filtro4.groupby("ciudad")["gasto_total"]
        .sum()
        .reset_index(name="sumatoria_gasto")
        .sort_values("sumatoria_gasto", ascending=False)
    )

    # FILTRO 5 — Usuarios inactivos → distribución por plan (para torta/mapa calor)
    filtro5 = data_frame_limpio.query("activo == False")
    agrupacion5 = (
        filtro5.groupby(["plan", "ciudad"])["id_users"]
        .count()
        .reset_index(name="conteo_inactivos")
    )

    transformacion_resumen = {
        "conteo_premium_por_ciudad":           agrupacion1,   # → barras / torta
        "gasto_promedio_activos_por_plan":     agrupacion2,   # → barras / torta
        "usuarios_alto_consumo_por_mes":       agrupacion3,   # → líneas
        "sumatoria_gasto_alto_por_ciudad":     agrupacion4,   # → barras / torta
        "inactivos_plan_ciudad":               agrupacion5,   # → mapa de calor
    }
    return transformacion_resumen


# ──────────────────────────────────────────────
# 3. VISUALIZACIONES
# ──────────────────────────────────────────────
COLORES = ["#4F86C6", "#F4845F", "#67B99A", "#A17FC0", "#F6C85F",
           "#E07B7B", "#6EC5E9", "#B5D99C", "#F5A7C7", "#7FCDCD"]

def _estilo_base():
    plt.rcParams.update({
        "figure.facecolor":  "#0F172A",
        "axes.facecolor":    "#1E293B",
        "axes.edgecolor":    "#334155",
        "axes.labelcolor":   "#CBD5E1",
        "xtick.color":       "#94A3B8",
        "ytick.color":       "#94A3B8",
        "text.color":        "#E2E8F0",
        "grid.color":        "#1E293B",
        "grid.linestyle":    "--",
        "grid.alpha":        0.4,
        "font.family":       "monospace",
    })


def graficar_barras(resumen: dict):
    _estilo_base()
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle("📊 Análisis de Usuarios — Barras", fontsize=16, fontweight="bold", color="#E2E8F0", y=1.01)
    fig.patch.set_facecolor("#0F172A")

    datasets = [
        ("conteo_premium_por_ciudad",       "ciudad",       "conteo_premium",       "Usuarios Premium por Ciudad"),
        ("gasto_promedio_activos_por_plan",  "plan",         "gasto_promedio",       "Gasto Promedio Activos por Plan"),
        ("usuarios_alto_consumo_por_mes",    "mes_registro", "usuarios_activos",     "Alto Consumo por Mes"),
        ("sumatoria_gasto_alto_por_ciudad",  "ciudad",       "sumatoria_gasto",      "Sumatoria Gasto ≥ 500k por Ciudad"),
    ]

    for ax, (key, col_x, col_y, titulo) in zip(axes.flat, datasets):
        df = resumen[key]
        bars = ax.bar(df[col_x], df[col_y], color=COLORES[:len(df)], edgecolor="#0F172A", linewidth=0.8)
        ax.set_title(titulo, fontsize=10, color="#94A3B8", pad=8)
        ax.set_xlabel(col_x, fontsize=8)
        ax.set_ylabel(col_y, fontsize=8)
        ax.tick_params(axis="x", rotation=35, labelsize=7)
        ax.yaxis.grid(True, alpha=0.3)
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h * 1.01,
                    f"{h:,.0f}", ha="center", va="bottom", fontsize=6.5, color="#CBD5E1")

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/grafica_barras.png", dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print("✅ Gráfica de barras guardada.")


def graficar_lineas(resumen: dict):
    _estilo_base()
    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor("#0F172A")

    df = resumen["usuarios_alto_consumo_por_mes"]
    ax.plot(df["mes_registro"], df["usuarios_activos"],
            marker="o", linewidth=2.5, color="#4F86C6",
            markerfacecolor="#F4845F", markeredgecolor="#0F172A", markersize=8)
    ax.fill_between(df["mes_registro"], df["usuarios_activos"], alpha=0.15, color="#4F86C6")

    ax.set_title("📈 Usuarios con Alto Consumo (>60 sesiones/mes) — Evolución Mensual",
                 fontsize=13, color="#E2E8F0", pad=12)
    ax.set_xlabel("Mes de Registro", fontsize=10)
    ax.set_ylabel("Cantidad de Usuarios", fontsize=10)
    ax.tick_params(axis="x", rotation=45, labelsize=8)
    ax.yaxis.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/grafica_lineas.png", dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print("✅ Gráfica de líneas guardada.")


def graficar_tortas(resumen: dict):
    _estilo_base()
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle("🥧 Distribución — Gráficas de Torta", fontsize=15, color="#E2E8F0", fontweight="bold")
    fig.patch.set_facecolor("#0F172A")

    # Torta 1 — Premium por ciudad
    df1 = resumen["conteo_premium_por_ciudad"]
    axes[0].pie(df1["conteo_premium"], labels=df1["ciudad"],
                colors=COLORES[:len(df1)], autopct="%1.1f%%",
                pctdistance=0.82, startangle=140,
                wedgeprops={"edgecolor": "#0F172A", "linewidth": 1.5},
                textprops={"color": "#CBD5E1", "fontsize": 8})
    axes[0].set_title("Usuarios Premium por Ciudad", color="#94A3B8", fontsize=10)

    # Torta 2 — Gasto promedio por plan
    df2 = resumen["gasto_promedio_activos_por_plan"]
    axes[1].pie(df2["gasto_promedio"], labels=df2["plan"],
                colors=COLORES[4:4+len(df2)], autopct="%1.1f%%",
                pctdistance=0.82, startangle=90,
                wedgeprops={"edgecolor": "#0F172A", "linewidth": 1.5},
                textprops={"color": "#CBD5E1", "fontsize": 9})
    axes[1].set_title("Gasto Promedio Activos por Plan", color="#94A3B8", fontsize=10)

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/grafica_tortas.png", dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print("✅ Gráfica de tortas guardada.")


def graficar_mapa_calor(resumen: dict):
    _estilo_base()
    df = resumen["inactivos_plan_ciudad"]

    pivot = df.pivot_table(index="plan", columns="ciudad",
                           values="conteo_inactivos", fill_value=0)

    fig, ax = plt.subplots(figsize=(16, 5))
    fig.patch.set_facecolor("#0F172A")

    cax = ax.imshow(pivot.values, aspect="auto", cmap="YlOrRd", interpolation="nearest")
    fig.colorbar(cax, ax=ax, label="Conteo de Inactivos")

    ax.set_xticks(range(len(pivot.columns)))
    ax.set_yticks(range(len(pivot.index)))
    ax.set_xticklabels(pivot.columns, rotation=40, ha="right", fontsize=9)
    ax.set_yticklabels(pivot.index, fontsize=10)

    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            val = pivot.values[i, j]
            ax.text(j, i, str(val), ha="center", va="center",
                    color="black" if val > pivot.values.max() * 0.6 else "white",
                    fontsize=8, fontweight="bold")

    ax.set_title("🌡️ Mapa de Calor — Usuarios Inactivos por Plan y Ciudad",
                 fontsize=13, color="#E2E8F0", pad=12)
    ax.set_xlabel("Ciudad", fontsize=10)
    ax.set_ylabel("Plan", fontsize=10)

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/grafica_mapa_calor.png", dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print("✅ Mapa de calor guardado.")


# ──────────────────────────────────────────────
# 4. MENÚ INTERACTIVO
# ──────────────────────────────────────────────
OPCIONES_GRAFICA = {
    "1": ("Barras",       graficar_barras),
    "2": ("Líneas",       graficar_lineas),
    "3": ("Tortas",       graficar_tortas),
    "4": ("Mapa de calor",graficar_mapa_calor),
}

def menu(resumen: dict):
    print("\n" + "═" * 45)
    print("  📊  VISUALIZADOR DE DATOS DE USUARIOS")
    print("═" * 45)
    for k, (nombre, _) in OPCIONES_GRAFICA.items():
        print(f"  [{k}] {nombre}")
    print("  [0] Salir")
    print("═" * 45)

    while True:
        opcion = input("\n  Seleccione una opción: ").strip()
        if opcion == "0":
            print("  👋 Hasta luego.")
            break
        elif opcion in OPCIONES_GRAFICA:
            _, funcion = OPCIONES_GRAFICA[opcion]
            funcion(resumen)
        else:
            print("  ⚠️  Opción inválida. Intente de nuevo.")


# ──────────────────────────────────────────────
# 5. EJECUCIÓN PRINCIPAL
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("⚙️  Generando dataset...")
    df = generar_dataset(500)

    print("🔄 Transformando datos...")
    resumen = transformar_datos(df)

    print("\n📋 Resumen de transformaciones:")
    for nombre, tabla in resumen.items():
        print(f"\n  ▸ {nombre}  ({len(tabla)} filas)")
        print(tabla.head(3).to_string(index=False))

    menu(resumen)