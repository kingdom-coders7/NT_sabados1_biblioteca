import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import random
from datetime import timedelta
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ──────────────────────────────────────────────
# 1. GENERACIÓN DEL DATASET DE PRÉSTAMOS
# ──────────────────────────────────────────────

def generar_tabla_prestamos(numero_registros: int = 500) -> pd.DataFrame:
    fake = Faker("es_CO")
    libros = [
        "Cien años de soledad", "El amor en los tiempos del cólera", "La sombra del viento",
        "Rayuela", "El principito", "1984", "Don Quijote de la Mancha", "El túnel",
        "Crónica de una muerte anunciada", "La casa de los espíritus", "Ficciones",
        "La ciudad y los perros", "Pedro Páramo", "La fiesta del chivo", "El otoño del patriarca",
        "El hombre en busca de sentido", "Sapiens", "Tokio blues", "El retrato de Dorian Gray", "Matar a un ruiseñor"
    ]
    usuarios = [fake.unique.random_number(digits=8) for _ in range(100)]
    registros = []

    for _ in range(numero_registros):
        fecha_inicio = fake.date_between(start_date="-2y", end_date="today")
        duracion = random.randint(3, 30)
        fecha_devolucion = fecha_inicio + timedelta(days=duracion)
        registros.append({
            "book_title": random.choice(libros),
            "id_users": random.choice(usuarios),
            "fecha_prestamo": fecha_inicio,
            "fecha_devolucion": fecha_devolucion,
            "duracion_dias": duracion,
        })

    df = pd.DataFrame(registros)
    df["fecha_prestamo"] = pd.to_datetime(df["fecha_prestamo"])
    df["fecha_devolucion"] = pd.to_datetime(df["fecha_devolucion"])
    return df


# ──────────────────────────────────────────────
# 2. TRANSFORMACIONES
# ──────────────────────────────────────────────

def transformar_datos(data_frame_limpio: pd.DataFrame) -> dict:
    libros_mas_prestados = (
        data_frame_limpio.groupby("book_title")["id_users"]
        .count()
        .reset_index(name="cantidad_prestamos")
        .sort_values("cantidad_prestamos", ascending=False)
    )

    usuarios_mas_prestamos = (
        data_frame_limpio.groupby("id_users")["book_title"]
        .count()
        .reset_index(name="cantidad_prestamos")
        .sort_values("cantidad_prestamos", ascending=False)
    )

    tiempo_promedio_por_libro = (
        data_frame_limpio.groupby("book_title")["duracion_dias"]
        .mean()
        .reset_index(name="duracion_promedio_dias")
        .sort_values("duracion_promedio_dias", ascending=False)
    )

    return {
        "libros_mas_prestados": libros_mas_prestados,
        "usuarios_mas_prestamos": usuarios_mas_prestamos,
        "tiempo_promedio_por_libro": tiempo_promedio_por_libro,
    }


# ──────────────────────────────────────────────
# 3. VISUALIZACIONES
# ──────────────────────────────────────────────
COLORES = ["#4F86C6", "#F4845F", "#67B99A", "#A17FC0", "#F6C85F",
           "#E07B7B", "#6EC5E9", "#B5D99C", "#F5A7C7", "#7FCDCD"]


def _estilo_base():
    plt.rcParams.update({
        "figure.facecolor": "#0F172A",
        "axes.facecolor": "#1E293B",
        "axes.edgecolor": "#334155",
        "axes.labelcolor": "#CBD5E1",
        "xtick.color": "#94A3B8",
        "ytick.color": "#94A3B8",
        "text.color": "#E2E8F0",
        "grid.color": "#1E293B",
        "grid.linestyle": "--",
        "grid.alpha": 0.4,
        "font.family": "monospace",
    })


def graficar_libros_mas_prestados(resumen: dict):
    _estilo_base()
    df = resumen["libros_mas_prestados"].head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(df["book_title"], df["cantidad_prestamos"], color=COLORES[: len(df)], edgecolor="#0F172A")
    ax.invert_yaxis()
    ax.set_title("📚 Libros más prestados", fontsize=14, color="#E2E8F0")
    ax.set_xlabel("Cantidad de préstamos", fontsize=10)
    ax.set_ylabel("Libro", fontsize=10)
    ax.xaxis.grid(True, alpha=0.3)

    for i, valor in enumerate(df["cantidad_prestamos"]):
        ax.text(valor + 0.5, i, str(valor), va="center", color="#E2E8F0", fontsize=8)

    plt.tight_layout()
    ruta = OUTPUT_DIR / "libros_mas_prestados.png"
    plt.savefig(ruta, dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print(f"✅ Guardado: {ruta}")


def graficar_usuarios_mas_prestamos(resumen: dict):
    _estilo_base()
    df = resumen["usuarios_mas_prestamos"].head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(df["id_users"].astype(str), df["cantidad_prestamos"], color=COLORES[: len(df)], edgecolor="#0F172A")
    ax.invert_yaxis()
    ax.set_title("👤 Usuarios con más préstamos", fontsize=14, color="#E2E8F0")
    ax.set_xlabel("Cantidad de préstamos", fontsize=10)
    ax.set_ylabel("ID de usuario", fontsize=10)
    ax.xaxis.grid(True, alpha=0.3)

    for i, valor in enumerate(df["cantidad_prestamos"]):
        ax.text(valor + 0.5, i, str(valor), va="center", color="#E2E8F0", fontsize=8)

    plt.tight_layout()
    ruta = OUTPUT_DIR / "usuarios_mas_prestamos.png"
    plt.savefig(ruta, dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print(f"✅ Guardado: {ruta}")


def graficar_tiempo_promedio_por_libro(resumen: dict):
    _estilo_base()
    df = resumen["tiempo_promedio_por_libro"].head(12)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["duracion_promedio_dias"], df["book_title"], marker="o", color="#4F86C6")
    ax.set_title("⏳ Tiempo promedio de préstamo por libro", fontsize=14, color="#E2E8F0")
    ax.set_xlabel("Duración promedio (días)", fontsize=10)
    ax.set_ylabel("Libro", fontsize=10)
    ax.xaxis.grid(True, alpha=0.3)
    ax.tick_params(axis="y", labelsize=9)

    plt.tight_layout()
    ruta = OUTPUT_DIR / "tiempo_promedio_por_libro.png"
    plt.savefig(ruta, dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print(f"✅ Guardado: {ruta}")


# ──────────────────────────────────────────────
# 4. MENÚ INTERACTIVO
# ──────────────────────────────────────────────
OPCIONES_GRAFICA = {
    "1": ("Libros más prestados", graficar_libros_mas_prestados),
    "2": ("Usuarios con más préstamos", graficar_usuarios_mas_prestamos),
    "3": ("Tiempo promedio de préstamo por libro", graficar_tiempo_promedio_por_libro),
}


def menu(resumen: dict):
    print("\n" + "═" * 45)
    print("  📈 VISUALIZADOR DE PRÉSTAMOS")
    print("═" * 45)
    for clave, (nombre, _) in OPCIONES_GRAFICA.items():
        print(f"  [{clave}] {nombre}")
    print("  [0] Salir")
    print("═" * 45)

    while True:
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        if opcion in OPCIONES_GRAFICA:
            _, funcion = OPCIONES_GRAFICA[opcion]
            funcion(resumen)
        else:
            print("Opción inválida. Intente de nuevo.")


# ──────────────────────────────────────────────
# 5. EJECUCIÓN PRINCIPAL
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("Generando tabla de préstamos...")
    df = generar_tabla_prestamos(500)

    print("Transformando datos...")
    resumen = transformar_datos(df)

    print("\nResumen de tablas:")
    for nombre, tabla in resumen.items():
        print(f"\n▸ {nombre} ({len(tabla)} registros)")
        print(tabla.head(5).to_string(index=False))

    menu(resumen)
