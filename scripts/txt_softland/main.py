import os
import pandas as pd
from typing import Literal

ANIO_MUESTRA = 2024

CONFIG_BANCOS = {
    "Banco Estado": {
        "renombrar_columnas": {
            "Fecha": "2024",
            "Operacion": "N° Operación",
        },
        "columnas_salida": [
            "12",
            "2024",
            "Descripcion corta",
            "N Doc.",
            "Cheques / Cargos",
            "Depósitos / Abonos",
        ],
        "columnas_numericas": [
            "Cheques / Cargos",
            "Depósitos / Abonos",
        ],
    },
    "Banco BCI": {
        "renombrar_columnas": {
            "Fecha": "2024",
            "N° Documento": "N° Operación",
            "Descripción": "Descripción",
            "Cheques y otros cargos": "Cheques / Cargos",
            "Depósitos y Abono": "Depósitos / Abonos",
        },
        "columnas_salida": [
            "12",
            "2024",
            "Descripcion corta",
            "N Doc.",
            "Cheques / Cargos",
            "Depósitos / Abonos",
        ],
        "columnas_numericas": [
            "Cheques y otros cargos",
            "Depósitos y Abono",
        ],
    },
    "Banco Itaú": {
        "renombrar_columnas": {
            "Fecha": "2024",
            "Sucursal": "N° Operación",
            "Descripción": "Descripción",
            "Giros o cargos": "Cheques / Cargos",
            "Depósitos o abonos": "Depósitos / Abonos",
        },
        "columnas_salida": [
            "12",
            "2024",
            "Descripcion corta",
            "N Doc.",
            "Cheques / Cargos",
            "Depósitos / Abonos",
        ],
        "columnas_numericas": [
            "Giros o cargos",
            "Depósitos o abonos",
        ],
    },
}


def agregar_anio(tabla: pd.DataFrame, columna_fecha: str) -> None:
    """
    Agrega año a fechas que no lo tengan en la columna especificada.
    """
    if columna_fecha in tabla.columns:
        anio_actual = ANIO_MUESTRA

        def agregar_anio(fecha: str) -> str:
            try:
                fecha_parseada = pd.to_datetime(
                    fecha,
                    format="%d/%m",
                    errors="coerce",
                )
                if pd.notnull(fecha_parseada):
                    return f"{fecha}/{anio_actual}"
                else:
                    return fecha
            except Exception:
                return fecha

        tabla[columna_fecha] = tabla[columna_fecha].apply(agregar_anio)


def agregar_columna_autoincremental(tabla, nombre_columna) -> None:
    """
    Agrega una columna autoincremental.
    """
    tabla.insert(0, nombre_columna, range(1, 1 + len(tabla)))


def renombrar_columnas(tabla, mapeo_columnas) -> None:
    """
    Renombra columnas en la tabla según un mapeo.
    """
    tabla.rename(columns=mapeo_columnas, inplace=True)


def generar_descripcion_corta(
    row,
) -> None | Literal["CH"] | Literal["DP"] | Literal["CB"]:
    """
    Genera la descripción corta basada en la descripción y montos.
    """
    descripcion: str = row["Descripción"].lower()
    cheques_cargos: int = row.get("Cheques / Cargos", 0)
    depositos_abonos: int = row.get("Depósitos / Abonos", 0)

    if "cheque" in descripcion:
        if cheques_cargos > 0:
            return "CH"
        elif depositos_abonos > 0:
            return "DP"
    elif cheques_cargos > 0:
        return "CB"
    elif depositos_abonos > 0:
        return "DP"
    return None


def agregar_descripcion_corta(tabla) -> None:
    """
    Agrega la columna Descripcion corta a la tabla.
    """
    tabla["Descripcion corta"] = tabla.apply(generar_descripcion_corta, axis=1)


def generar_n_doc(row) -> int | None:
    """
    Genera el valor de la columna N Doc.
    """
    descripcion_corta = row["Descripcion corta"]
    fecha = row["2024"]
    n_operacion = row["N° Operación"]

    try:
        if descripcion_corta == "CH":
            return int(n_operacion)
        elif descripcion_corta in ["CB", "DP"]:
            if isinstance(fecha, str):
                fecha = pd.to_datetime(fecha, errors="coerce", dayfirst=True)
            if pd.notnull(fecha):
                day: int = fecha.day
                month: int = fecha.month
                return int(f"{day:02}{month:02}")
        return None
    except ValueError:
        return None


def agregar_n_doc(tabla) -> None:
    """
    Agrega la columna `N Doc.` a la tabla.
    """
    tabla["N Doc."] = tabla.apply(generar_n_doc, axis=1)


def convertir_columnas(tabla: pd.DataFrame, columnas: list) -> None:
    """
    Convierte las columnas a tipo numérico y rellena los valores vacíos con 0.
    """
    for columna in columnas:
        if columna in tabla.columns:
            tabla[columna] = tabla[columna].replace(
                {r"\.": "", r"\$": ""},
                regex=True,
            )
            tabla[columna] = pd.to_numeric(
                tabla[columna],
                errors="coerce",
            ).fillna(0)


def procesar_banco(nombre_banco, ruta_entrada, ruta_salida) -> None:
    """
    Procesa archivo según la config del banco.
    """
    if nombre_banco not in CONFIG_BANCOS:
        raise ValueError(f"Config no encontrada para: {nombre_banco}")

    config = CONFIG_BANCOS[nombre_banco]

    # Detectar el tipo de archivo
    extension = os.path.splitext(ruta_entrada)[1].lower()
    if extension == ".xlsx":
        data = pd.read_excel(ruta_entrada)
    else:
        raise ValueError("El archivo debe ser .xlsx")

    nueva_tabla: pd.DataFrame = data.copy()

    # Agregar el año a las fechas si falta
    agregar_anio(nueva_tabla, "Fecha")

    # Convertir las columnas a numérico
    convertir_columnas(nueva_tabla, config["columnas_numericas"])

    # Procesar datos
    agregar_columna_autoincremental(nueva_tabla, "12")
    renombrar_columnas(nueva_tabla, config["renombrar_columnas"])
    agregar_descripcion_corta(nueva_tabla)
    agregar_n_doc(nueva_tabla)

    # Filtrar columnas necesarias
    resultado_tabla: pd.DataFrame = nueva_tabla[config["columnas_salida"]]

    # Guardar resultado
    resultado_tabla.to_excel(ruta_salida, index=False)
    print(f"Archivo guardado como '{ruta_salida}'.")


def main() -> None:
    """
    Script principal.
    """
    print("Seleccione el banco para procesar:")
    try:
        for i, banco in enumerate(CONFIG_BANCOS.keys(), start=1):
            print(f"{i}. {banco}")

        opcion = int(input("Ingresa número del banco: "))
        bancos = list(CONFIG_BANCOS.keys())

        if opcion < 1 or opcion > len(bancos):
            print("Opción inválida.")
            return

        nombre_banco: str = bancos[opcion - 1]
        ruta_entrada: str = input("Ingresa ruta del archivo (Entrada): ")
        ruta_salida: str = input("Ingresa ruta del archivo (Salida): ")

        procesar_banco(nombre_banco, ruta_entrada, ruta_salida)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
