import pandas as pd
import glob
from typing import List


def cargar_datos_movimientos(ruta_archivos: str) -> pd.DataFrame:
    """
    Carga y combina los datos de x hoja desde múltiples archivos.
    """
    archivos_excel: List[str] = glob.glob(ruta_archivos)
    if not archivos_excel:
        raise FileNotFoundError(
            f"No se encontraron archivos en la ruta: {ruta_archivos}"
        )

    datos_combinados: List[pd.DataFrame] = []

    for archivo in archivos_excel:
        try:
            df: pd.DataFrame = pd.read_excel(archivo, sheet_name="Movimientos")
            datos_combinados.append(df)
            print(f"Datos cargados correctamente desde: {archivo}")
        except ValueError:
            print(f"La hoja no se encontró en el archivo: {archivo}")
        except Exception as e:
            print(f"Error al leer el archivo {archivo}: {e}")

    if not datos_combinados:
        raise ValueError("No se encontraron datos en ninguna hoja.")

    return pd.concat(datos_combinados, ignore_index=True)


def guardar_datos(df: pd.DataFrame, archivo_salida: str) -> None:
    """
    Guarda un DataFrame en un archivo Excel.
    """
    try:
        df.to_excel(archivo_salida, index=False)
        print(f"Archivo combinado guardado como: {archivo_salida}")
    except Exception as e:
        print(f"Error al guardar el archivo: {archivo_salida}. Detalle: {e}")


def main() -> None:
    """
    Función principal del script.
    """
    ruta_archivos = "*.xlsx"
    archivo_salida = "Movimientos_Combinados.xlsx"

    try:
        df_combinado: pd.DataFrame = cargar_datos_movimientos(ruta_archivos)
        guardar_datos(df_combinado, archivo_salida)
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")


if __name__ == "__main__":
    main()
