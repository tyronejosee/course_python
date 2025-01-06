import os
import pandas as pd
import glob
from termcolor import colored
import pyfiglet


def listar_archivos(ruta_archivos):
    """
    Lista todos los archivos disponibles en la ruta.
    """
    archivos_excel = glob.glob(ruta_archivos)
    if not archivos_excel:
        print(colored("No se encontraron archivos en la ruta especificada.", "red"))
        return []

    print(colored("Archivos encontrados:", "blue", attrs=["bold"]))
    for archivo in archivos_excel:
        print(colored(f" - {archivo}", "white"))
    return archivos_excel


def cargar_datos_movimientos(ruta_archivos, nombre_hoja, archivo_ignorado):
    """
    Carga y combina los datos de la hoja desde múltiples archivos.
    """
    archivos_excel = glob.glob(ruta_archivos)
    if not archivos_excel:
        raise FileNotFoundError(
            f"No se encontraron archivos en la ruta: {ruta_archivos}"
        )

    # Filtrar el archivo a ignorar
    archivos_excel = [
        archivo
        for archivo in archivos_excel
        if os.path.basename(archivo) != archivo_ignorado
    ]

    if not archivos_excel:
        raise FileNotFoundError("No se encontraron archivos válidos.")

    datos_combinados = []

    for archivo in archivos_excel:
        try:
            df = pd.read_excel(archivo, sheet_name=nombre_hoja)
            datos_combinados.append(df)
            mensaje = f"Datos cargados correctamente desde: {archivo}"
            print(colored(mensaje, "green", attrs=["bold"]))
        except ValueError:
            mensaje = f"La hoja no se encontró en el archivo: {archivo}"
            print(colored(mensaje, "yellow", attrs=["bold"]))
        except Exception as e:
            mensaje = f"Error al leer el archivo {archivo}: {e}"
            print(colored(mensaje, "red", attrs=["bold"]))

    if not datos_combinados:
        raise ValueError("No se encontraron datos en ninguna hoja.")

    return pd.concat(datos_combinados, ignore_index=True)


def guardar_datos(df, archivo_salida):
    """
    Guarda un DataFrame en un archivo Excel.
    """
    try:
        df.to_excel(archivo_salida, index=False)
        mensaje = f"\n🎉 Archivo guardado como {archivo_salida}\n"
        print(colored(mensaje, "white", attrs=["bold"]))
    except Exception as e:
        mensaje = f"Error al guardar: {archivo_salida} - {e}"
        print(colored(mensaje, "red", attrs=["bold"]))


def main():
    """
    Función principal del script.
    """
    ruta_archivos = "*.xlsx"
    autor = "by https://github.com/tyronejosee\n"

    arte = pyfiglet.figlet_format("XLSXMerger")
    print()
    print(colored(arte, "blue", attrs=["bold"]))
    print(colored(autor, "dark_grey", attrs=["bold"]))

    while True:
        print("\nOpciones:")
        print("1. Listar archivos disponibles")
        print("2. Combinar archivos")
        print("3. Salir")

        opcion = input(
            colored("\nSelecciona una opción: ", "yellow", attrs=["bold"])
        ).strip()

        if opcion == "1":
            listar_archivos(ruta_archivos)

        elif opcion == "2":
            nombre_salida = input(
                colored(
                    "\nIngresa nombre del archivo salida (sin extensión): ",
                    "yellow",
                    attrs=["bold"],
                )
            ).strip()
            nombre_hoja = input(
                colored(
                    "\nIngresa nombre de hoja: ",
                    "yellow",
                    attrs=["bold"],
                )
            ).strip()
            archivo_salida = f"{nombre_salida}.xlsx"

            try:
                df_combinado = cargar_datos_movimientos(
                    ruta_archivos,
                    nombre_hoja,
                    archivo_salida,
                )
                guardar_datos(df_combinado, archivo_salida)
            except Exception as e:
                print(colored(f"Error: {e}", "red"))

        elif opcion == "3":
            print(
                colored(
                    "\n👋 ¡Hasta luego!",
                    "green",
                    attrs=["bold"],
                )
            )
            break

        else:
            print(colored("\nOpción no válida. Intenta de nuevo.", "red"))


if __name__ == "__main__":
    main()
