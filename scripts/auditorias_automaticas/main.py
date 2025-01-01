"""
Auditorías Automáticas:
- Detectar transacciones duplicadas o sospechosas.
- Identificar registros faltantes.
"""

import pandas as pd


def cargar_datos(archivo):
    """Carga los datos financieros desde un archivo CSV."""
    try:
        datos = pd.read_csv(archivo)
        print(f"Datos cargados desde {archivo}")
        return datos
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None


def detectar_duplicados(datos):
    """Detecta transacciones duplicadas en los datos."""
    duplicados = datos[datos.duplicated(keep=False)]
    if not duplicados.empty:
        print("Transacciones duplicadas encontradas:")
        print(duplicados)
    else:
        print("No se encontraron transacciones duplicadas.")
    return duplicados


def detectar_sospechosos(datos, columna_monto, umbral):
    """Detecta transacciones sospechosas basadas en un umbral de monto."""
    sospechosos = datos[datos[columna_monto] > umbral]
    if not sospechosos.empty:
        print(f"Transacciones sospechosas con montos mayores a {umbral}:")
        print(sospechosos)
    else:
        print("No se encontraron transacciones sospechosas.")
    return sospechosos


def identificar_registros_faltantes(datos, columnas_obligatorias):
    """Identifica registros con valores faltantes en las columnas obligatorias."""
    faltantes = datos[datos[columnas_obligatorias].isnull().any(axis=1)]
    if not faltantes.empty:
        print("Registros con datos faltantes encontrados:")
        print(faltantes)
    else:
        print("No se encontraron registros con datos faltantes.")
    return faltantes


def guardar_resultados(resultado, nombre_archivo):
    """Guarda los resultados en un archivo CSV."""
    if not resultado.empty:
        resultado.to_csv(nombre_archivo, index=False, encoding="utf-8-sig")
        print(f"Resultados guardados en {nombre_archivo}")
    else:
        print(f"No hay resultados para guardar en {nombre_archivo}.")


# Ruta del archivo CSV a auditar
archivo_datos = input("Ingrese la ruta del archivo CSV con los datos financieros: ")
datos = cargar_datos(archivo_datos)

if datos is not None:
    # Detectar duplicados
    duplicados = detectar_duplicados(datos)
    guardar_resultados(duplicados, "duplicados.csv")

    # Detectar transacciones sospechosas
    columna_monto = input("Ingrese el nombre de la columna de montos: ")
    umbral = float(input("Ingrese el umbral para transacciones sospechosas: "))
    sospechosos = detectar_sospechosos(datos, columna_monto, umbral)
    guardar_resultados(sospechosos, "sospechosos.csv")

    # Identificar registros faltantes
    columnas_obligatorias = input(
        "Ingrese las columnas obligatorias separadas por comas: "
    ).split(",")
    faltantes = identificar_registros_faltantes(
        datos, [col.strip() for col in columnas_obligatorias]
    )
    guardar_resultados(faltantes, "faltantes.csv")

    print("Auditoría completada.")
