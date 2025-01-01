"""
Libro Diario:
- Automatizar la generación y verificación de balances entre `Debe` y `Haber`.
- Cargar o guardar los datos desde/para Excel.
"""

import pandas as pd


def leer_libro_diario(ruta_archivo):
    """
    Lee el libro diario desde un archivo Excel.
    """
    try:
        diario_df = pd.read_excel(ruta_archivo)
        print(f"Libro diario cargado exitosamente desde: {ruta_archivo}")
        return diario_df
    except FileNotFoundError:
        raise FileNotFoundError(
            f"El archivo {ruta_archivo} no se encontró. Verifica la ruta."
        )
    except Exception as e:
        raise Exception(f"Error al leer el archivo: {e}")


def verificar_balance(diario_df):
    """
    Verifica que el balance entre Debe y Haber esté cuadrado por asiento.
    """
    if not all(
        col in diario_df.columns for col in ["Número de Asiento", "Debe", "Haber"]
    ):
        raise ValueError(
            "El libro diario debe contener las columnas 'Número de Asiento', 'Debe' y 'Haber'."
        )

    # Calcular el balance
    diario_df["Balance"] = diario_df["Debe"] - diario_df["Haber"]
    balance_cuadrado = (
        diario_df.groupby("Número de Asiento")["Balance"].sum().eq(0).all()
    )

    if balance_cuadrado:
        print("El libro diario está cuadrado.")
    else:
        print("Hay desbalances en el libro diario.")

    return diario_df, balance_cuadrado


def guardar_libro_diario(diario_df, ruta_salida):
    """
    Guarda el libro diario con los balances verificados en un archivo Excel.
    """
    try:
        diario_df.to_excel(ruta_salida, index=False, engine="openpyxl")
        print(
            f"Libro diario verificado guardado exitosamente en: {ruta_salida}",
        )
    except Exception as e:
        raise Exception(f"Error al guardar el archivo: {e}")


if __name__ == "__main__":
    try:
        # Ruta de entrada y salida
        ruta_archivo = "libro_diario.xlsx"
        ruta_salida = "libro_diario_verificado.xlsx"

        # Leer el libro diario
        diario_df = leer_libro_diario(ruta_archivo)

        # Verificar balances
        diario_df, balance_cuadrado = verificar_balance(diario_df)

        # Guardar los resultados
        guardar_libro_diario(diario_df, ruta_salida)
    except Exception as e:
        print(f"Error en el proceso: {e}")
