"""
Script para procesar un archivo Excel con info de cuentas contables.
"""

import pandas as pd
from constants import (
    ARCHIVO_ENTRADA,
    ARCHIVO_SALIDA,
    NOMBRE_HOJA,
    COLUMNA_FICHA,
    COLUMNA_NUMERO,
    COLUMNA_ABONOS,
    COLUMNA_CARGOS,
    COLUMNA_SALDO,
    COLUMNA_PIVOTE,
    COLUMNAS_NECESARIAS,
    VARIOS,
)


def procesar_excel(input_file, output_file):
    # Leer la hoja específica "proveedores nacionales" del archivo Excel
    try:
        df = pd.read_excel(input_file, sheet_name=NOMBRE_HOJA)
    except ValueError:
        raise ValueError("La hoja no existe en el archivo Excel.")

    # Verificar si las columnas necesarias están presentes
    if not all(col in df.columns for col in COLUMNAS_NECESARIAS):
        raise ValueError(f"Faltan columnas necesarias: {COLUMNAS_NECESARIAS}")

    # Convertir las columnas Abonos, Cargos y Saldo a numéricas
    for col in [COLUMNA_ABONOS, COLUMNA_CARGOS, COLUMNA_SALDO]:
        df[col] = df[col].replace({",": ""}, regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Filtrar las filas donde Ficha no sea VARIOS
    df = df[df[COLUMNA_FICHA] != VARIOS]

    # Agrupar por Ficha y Número
    df[COLUMNA_PIVOTE] = df[COLUMNA_SALDO].abs()
    df_grouped = df.groupby([COLUMNA_FICHA, COLUMNA_NUMERO, COLUMNA_PIVOTE])

    # Identificar y eliminar pares de saldos positivos y negativos
    indices_a_eliminar = []
    for _, group in df_grouped:
        if len(group) == 2 and group[COLUMNA_SALDO].sum() == 0:
            indices_a_eliminar.extend(group.index)

    # Crear un nuevo DataFrame eliminando las filas seleccionadas por saldo
    df_filtrado = df.drop(indices_a_eliminar)

    # Agrupar nuevamente por Ficha y Número para realizar el nuevo filtro
    df_grouped = df_filtrado.groupby([COLUMNA_FICHA, COLUMNA_NUMERO])

    # Eliminar filas donde la suma de Abonos menos Cargos es igual a 0
    indices_a_eliminar_por_abonos_cargos = []
    for _, group in df_grouped:
        if (group[COLUMNA_ABONOS].sum() - group[COLUMNA_CARGOS].sum()) == 0:
            indices_a_eliminar_por_abonos_cargos.extend(group.index)

    # Crear un nuevo DF eliminando las filas por abonos y cargos
    df_filtrado: pd.DataFrame = df_filtrado.drop(
        indices_a_eliminar_por_abonos_cargos,
    )

    # Guardar el resultado en un nuevo archivo Excel
    df_filtrado.to_excel(output_file, index=False)
    print(f"Archivo guardado en: {output_file}")


if __name__ == "__main__":
    procesar_excel(ARCHIVO_ENTRADA, ARCHIVO_SALIDA)
