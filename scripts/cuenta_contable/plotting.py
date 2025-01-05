"""
Plotting script for Excel data
"""

import pandas as pd
import matplotlib.pyplot as plt

from constants import (
    ARCHIVO_PLOTTING,
    COLUMNA_ABONOS,
    COLUMNA_CARGOS,
    COLUMNA_FICHA,
    COLUMNAS_NECESARIAS,
    NOMBRE_HOJA_PLOTTING,
)


def procesar_y_graficar_excel(input_file) -> None:
    try:
        df: pd.DataFrame = pd.read_excel(input_file, sheet_name=NOMBRE_HOJA_PLOTTING)
    except ValueError as e:
        print(f"Error leyendo el archivo Excel: {e}")

    # Verificar columnas necesarias
    if not all(col in df.columns for col in COLUMNAS_NECESARIAS):
        print(f"Faltan columnas necesarias: {COLUMNAS_NECESARIAS}")
        return

    # Asegurarse de que las columnas sean numéricas
    for col in [COLUMNA_ABONOS, COLUMNA_CARGOS]:
        df[col] = df[col].replace({",": ""}, regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Eliminar filas con valores NaN en las columnas necesarias
    df = df.dropna(subset=[COLUMNA_FICHA, COLUMNA_ABONOS, COLUMNA_CARGOS])

    # Agrupar por Ficha y calcular totales
    agrupado: pd.DataFrame = df.groupby(COLUMNA_FICHA).agg(
        {COLUMNA_ABONOS: "sum", COLUMNA_CARGOS: "sum"}
    )

    # Abreviar nombres largos de fichas
    agrupado.index = agrupado.index.str.split().str[0:2].str.join(" ")

    # Graficar los datos
    # fichas = agrupado.index
    # abonos = agrupado[COLUMNA_ABONOS]
    # cargos = agrupado[COLUMNA_CARGOS]

    # plt.figure(figsize=(10, 4))
    # plt.bar(fichas, abonos, label="Abonos", color="skyblue")
    # plt.bar(fichas, cargos, label="Cargos", bottom=abonos, color="lightcoral")

    # # Etiquetas y leyenda
    # plt.xlabel("Ficha")
    # plt.ylabel("Monto Total")
    # plt.title("Totales de Abonos y Cargos por Ficha")
    # plt.legend()
    # plt.xticks(rotation=30, fontsize=4, ha="right")
    # # plt.xticks(rotation=45, ha="right")
    # plt.tight_layout()
    # plt.show()

    # Gráfico de torta
    # Suma de Abonos y Cargos totales
    totales = agrupado.sum(axis=0)
    plt.figure(figsize=(8, 8))
    plt.pie(
        totales,
        labels=["Abonos", "Cargos"],
        autopct="%1.1f%%",
        colors=["skyblue", "lightcoral"],
        startangle=140,
    )
    plt.title("Distribución de Abonos y Cargos Totales")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    procesar_y_graficar_excel(ARCHIVO_PLOTTING)
