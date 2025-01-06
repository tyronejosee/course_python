import os
import pandas as pd
from termcolor import colored
import pyfiglet


ANIO_MUESTRA = 2024

CONFIG_BANCOS = {
    "Banco Estado": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "N° Operación": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Cheques / Cargos": "CHEQUES_CARGOS",
            "Depósitos / Abonos": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cheques / Cargos",
            "Depósitos / Abonos",
        ],
    },
    "Banco BCI": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "N° Documento": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Cheques y otros cargos": "CHEQUES_CARGOS",
            "Depósitos y Abono": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cheques y otros cargos",
            "Depósitos y Abono",
        ],
    },
    "Banco Itaú": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "Sucursal": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Giros o cargos": "CHEQUES_CARGOS",
            "Depósitos o abonos": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Giros o cargos",
            "Depósitos o abonos",
        ],
    },
    "Banco de Chile": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "Docto. Nro.": "N_DOCUMENTO",
            "Detalle Movimiento": "DESCRIPCION",
            "Cheque o Cargo": "CHEQUES_CARGOS",
            "Deposito o Abono": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cheque o Cargo",
            "Deposito o Abono",
        ],
    },
    "Banco Scotiabank": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "Numero Documento": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Cargo": "CHEQUES_CARGOS",
            "Abono": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cargo",
            "Abono",
        ],
    },
}


def agregar_anio(tabla, columna_fecha):
    # Agrega año a fechas que no lo tengan en la columna especificada.
    if columna_fecha in tabla.columns:
        anio_actual = ANIO_MUESTRA

        def agregar_anio(fecha):
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


def agregar_columna_autoincremental(tabla, nombre_columna="INDEX"):
    # Agrega una columna autoincremental.
    tabla.insert(0, nombre_columna, range(1, 1 + len(tabla)))


def renombrar_columnas(tabla, mapeo_columnas):
    # Renombra columnas en la tabla según un mapeo.
    tabla.rename(columns=mapeo_columnas, inplace=True)


def generar_descripcion_corta(tabla):
    # Genera la descripción corta basada en la descripción y montos.
    descripcion = tabla["DESCRIPCION"].lower()
    cheques_cargos = tabla.get("CHEQUES_CARGOS", 0)
    depositos_abonos = tabla.get("DEPOSITOS_ABONOS", 0)

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


def agregar_descripcion_corta(tabla):
    # Agrega la columna Descripcion corta a la tabla.
    tabla["DESCRIPCION"] = tabla.apply(generar_descripcion_corta, axis=1)


def generar_n_doc(tabla):
    # Genera el valor de la columna N Doc.
    descripcion_corta = tabla["DESCRIPCION"]
    fecha = tabla["FECHA"]
    n_operacion = tabla["N_DOCUMENTO"]

    try:
        if descripcion_corta == "CH":
            return int(n_operacion)
        elif descripcion_corta in ["CB", "DP"]:
            if isinstance(fecha, str):
                fecha = pd.to_datetime(fecha, errors="coerce", dayfirst=True)
            if pd.notnull(fecha):
                day = fecha.day
                month = fecha.month
                return int(f"{day:02}{month:02}")
        return None
    except ValueError:
        return None


def agregar_n_doc(tabla):
    # Agrega la columna N_OPERACION a la tabla.
    tabla["N_OPERACION"] = tabla.apply(generar_n_doc, axis=1)


def convertir_columnas(tabla, columnas):
    # Convierte las columnas a numérico y rellena los valores vacíos con 0.
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


def procesar_banco(nombre_banco, ruta_entrada, ruta_salida):
    # Procesa archivo según la config del banco.
    if nombre_banco not in CONFIG_BANCOS:
        raise ValueError(f"Config no encontrada para: {nombre_banco}")

    config = CONFIG_BANCOS[nombre_banco]

    # Detectar el tipo de archivo
    extension = os.path.splitext(ruta_entrada)[1].lower()
    if extension == ".xlsx":
        data = pd.read_excel(ruta_entrada)
    else:
        raise ValueError("El archivo debe ser .xlsx")

    nueva_tabla = data.copy()

    # Agregar el año a las fechas si falta
    nueva_tabla["Fecha"] = pd.to_datetime(nueva_tabla["Fecha"], dayfirst=True)
    nueva_tabla["Fecha"] = nueva_tabla["Fecha"].dt.strftime("%d/%m/%Y")
    agregar_anio(nueva_tabla, "Fecha")

    # Convertir las columnas a numérico
    convertir_columnas(nueva_tabla, config["columnas_numericas"])

    # Procesar datos
    renombrar_columnas(nueva_tabla, config["renombrar_columnas"])
    agregar_columna_autoincremental(nueva_tabla)
    agregar_descripcion_corta(nueva_tabla)
    agregar_n_doc(nueva_tabla)

    # Filtrar columnas necesarias
    resultado_tabla = nueva_tabla[config["columnas_salida"]]

    # Guardar resultado
    resultado_tabla.to_excel(ruta_salida, index=False)
    print(
        colored(
            f"\n🎉 Archivo guardado como {ruta_salida}.\n",
            "green",
            attrs=["bold"],
        )
    )


def print_input(tipo, texto, color):
    data = tipo(input(colored(texto, color, attrs=["bold"])))
    return data


def print_output(texto, color):
    print(colored(texto, color, attrs=["bold"]))


def main():
    try:
        print()
        arte = pyfiglet.figlet_format("SoftlandTXT")
        print_output(arte, "blue")
        print_output("by https://github.com/tyronejosee\n", "dark_grey")

        print_output("Seleccione el banco para procesar:\n", "yellow")
        for i, banco in enumerate(CONFIG_BANCOS.keys(), start=1):
            print_output(f"[ {i} ] {banco}", "white")

        opcion = print_input(int, "\nIngresa número del banco: ", "yellow")
        bancos = list(CONFIG_BANCOS.keys())
        if opcion < 1 or opcion > len(bancos):
            print_output("Opción inválida.", "red")
            return
        nombre_banco = bancos[opcion - 1]

        ruta_entrada = print_input(
            str, "Ingresa ruta del archivo (Entrada): ", "yellow"
        )
        ruta_entrada = f"{ruta_entrada}.xlsx"

        ruta_salida = print_input(
            str,
            "Ingresa rutas del archivo (Salida): ",
            "yellow",
        )
        ruta_salida = f"{ruta_salida}.xlsx"

        procesar_banco(nombre_banco, ruta_entrada, ruta_salida)
    except Exception as e:
        print(colored(f"Error: {e}\n", "red", attrs=["bold"]))


if __name__ == "__main__":
    main()
