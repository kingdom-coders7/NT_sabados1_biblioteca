import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import random
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ──────────────────────────────────────────────
# 1. GENERACIÓN DEL DATASET
# ──────────────────────────────────────────────

def generar_dataset(numero_usuarios: int = 500) -> pd.DataFrame:
    fake = Faker("es_CO")
    dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
                "Bucaramanga", "Pereira", "Manizales", "Cúcuta", "Ibagué"]
    planes = ["básico", "estándar", "premium", "empresarial"]

    registros = []
    for _ in range(numero_usuarios):
        fecha_registro = fake.date_between(start_date="-2y", end_date="today")
        nombre_usuario = fake.user_name().lower().replace(" ", "_")
        dominio = random.choice(dominios)
        registros.append({
            "id_users": fake.unique.random_number(digits=8),
            "name": fake.first_name(),
            "last_name": fake.last_name(),
            "movil": fake.phone_number(),
            "email": f"{nombre_usuario}@{dominio}",
            "dominio": dominio,
            "ciudad": random.choice(ciudades),
            "fecha_registro": fecha_registro,
            "fecha_registro_dia": fecha_registro,
            "plan": random.choice(planes),
            "activo": random.choice([True, False]),
            "sesiones_mes": random.randint(0, 120),
            "gasto_total": round(random.uniform(0, 2_000_000), 2),
        })

    df = pd.DataFrame(registros)
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])
    df["fecha_registro_dia"] = pd.to_datetime(df["fecha_registro_dia"]).dt.date
    return df


# ──────────────────────────────────────────────
# 2. TRANSFORMACIONES
# ──────────────────────────────────────────────

def transformar_datos(data_frame_limpio: pd.DataFrame) -> dict:
    usuarios_por_ciudad = (
        data_frame_limpio.groupby("ciudad")["id_users"]
        .count()
        .reset_index(name="cantidad_usuarios")
        .sort_values("cantidad_usuarios", ascending=False)
    )

    usuarios_por_fecha = (
        data_frame_limpio.groupby("fecha_registro_dia")["id_users"]
        .count()
        .reset_index(name="cantidad_usuarios")
        .sort_values("fecha_registro_dia")
    )

    usuarios_por_dominio = (
        data_frame_limpio.groupby("dominio")["id_users"]
        .count()
        .reset_index(name="cantidad_usuarios")
        .sort_values("cantidad_usuarios", ascending=False)
    )

    return {
        "usuarios_por_ciudad": usuarios_por_ciudad,
        "usuarios_por_fecha": usuarios_por_fecha,
        "usuarios_por_dominio": usuarios_por_dominio,
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


def graficar_usuarios_por_ciudad(resumen: dict):
    _estilo_base()
    df = resumen["usuarios_por_ciudad"]
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df["ciudad"], df["cantidad_usuarios"], color=COLORES[: len(df)], edgecolor="#0F172A")
    ax.set_title("📍 Cantidad de usuarios por ciudad", fontsize=14, color="#E2E8F0")
    ax.set_xlabel("Ciudad", fontsize=10)
    ax.set_ylabel("Usuarios", fontsize=10)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.yaxis.grid(True, alpha=0.3)

    for i, valor in enumerate(df["cantidad_usuarios"]):
        ax.text(i, valor + 0.5, str(valor), ha="center", va="bottom", color="#E2E8F0", fontsize=8)

    plt.tight_layout()
    ruta = OUTPUT_DIR / "usuarios_por_ciudad.png"
    plt.savefig(ruta, dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print(f"✅ Guardado: {ruta}")


def graficar_usuarios_por_fecha(resumen: dict):
    _estilo_base()
    df = resumen["usuarios_por_fecha"]
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df["fecha_registro_dia"], df["cantidad_usuarios"], marker="o", color="#4F86C6", linewidth=2)
    ax.fill_between(df["fecha_registro_dia"], df["cantidad_usuarios"], alpha=0.15, color="#4F86C6")
    ax.set_title("📅 Usuarios registrados por fecha", fontsize=14, color="#E2E8F0")
    ax.set_xlabel("Fecha de registro", fontsize=10)
    ax.set_ylabel("Usuarios", fontsize=10)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.yaxis.grid(True, alpha=0.3)

    plt.tight_layout()
    ruta = OUTPUT_DIR / "usuarios_por_fecha.png"
    plt.savefig(ruta, dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print(f"✅ Guardado: {ruta}")


def graficar_usuarios_por_dominio(resumen: dict):
    _estilo_base()
    df = resumen["usuarios_por_dominio"]
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(df["cantidad_usuarios"], labels=df["dominio"], autopct="%1.1f%%",
           colors=COLORES[: len(df)], textprops={"color": "#FFFFFF", "fontsize": 9}, startangle=140)
    ax.set_title("📧 Usuarios registrados por tipo de dominio", fontsize=14, color="#E2E8F0")
    plt.tight_layout()
    ruta = OUTPUT_DIR / "usuarios_por_dominio.png"
    plt.savefig(ruta, dpi=150, bbox_inches="tight", facecolor="#0F172A")
    plt.show()
    print(f"✅ Guardado: {ruta}")


# ──────────────────────────────────────────────
# 4. MENÚ INTERACTIVO
# ──────────────────────────────────────────────
OPCIONES_GRAFICA = {
    "1": ("Cantidad de usuarios por ciudad", graficar_usuarios_por_ciudad),
    "2": ("Usuarios registrados por fecha", graficar_usuarios_por_fecha),
    "3": ("Usuarios registrados por tipo de dominio", graficar_usuarios_por_dominio),
}


def menu(resumen: dict):
    print("\n" + "═" * 45)
    print("  📊 VISUALIZADOR DE USUARIOS")
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
    print("Generando dataset de usuarios...")
    df = generar_dataset(500)

    print("Transformando datos...")
    resumen = transformar_datos(df)

    print("\nResumen de tablas:")
    for nombre, tabla in resumen.items():
        print(f"\n▸ {nombre} ({len(tabla)} registros)")
        print(tabla.head(5).to_string(index=False))

    menu(resumen)
