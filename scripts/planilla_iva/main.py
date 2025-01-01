"""
Planilla de IVA:
- Calcular automáticamente el IVA débito y crédito fiscal,
  y determinar el IVA a pagar.
"""

import pandas as pd


def leer_planilla_iva(ruta_archivo):
    """
    Lee la planilla de IVA desde un archivo Excel.
    """
    try:
        iva_df = pd.read_excel(ruta_archivo)
        print(f"Planilla de IVA cargada exitosamente desde: {ruta_archivo}")
        return iva_df
    except FileNotFoundError:
        raise FileNotFoundError(
            f"El archivo {ruta_archivo} no se encontró. Verifica la ruta."
        )
    except Exception as e:
        raise Exception(f"Error al leer el archivo: {e}")


def calcular_iva(iva_df):
    """
    Calcula el IVA débito, crédito fiscal, y el IVA a pagar.
    """
    try:
        if "Tipo de IVA" not in iva_df.columns or "IVA (19%)" not in iva_df.columns:
            raise ValueError(
                "La planilla debe contener las columnas 'Tipo de IVA' e 'IVA (19%)'."
            )

        iva_debito = iva_df.loc[
            iva_df["Tipo de IVA"] == "Débito Fiscal", "IVA (19%)"
        ].sum()
        iva_credito = iva_df.loc[
            iva_df["Tipo de IVA"] == "Crédito Fiscal", "IVA (19%)"
        ].sum()
        iva_a_pagar = iva_debito - iva_credito

        print(
            f"IVA Débito: {iva_debito}, IVA Crédito: {iva_credito}, IVA a Pagar: {iva_a_pagar}"
        )
        return iva_debito, iva_credito, iva_a_pagar
    except Exception as e:
        raise Exception(f"Error durante el cálculo de IVA: {e}")


def guardar_resultados(iva_df, iva_a_pagar, ruta_salida):
    """
    Guarda el cálculo del IVA en un archivo Excel.
    """
    try:
        iva_df["IVA a Pagar"] = iva_a_pagar
        iva_df.to_excel(ruta_salida, index=False, engine="openpyxl")
        print(f"Cálculos guardados exitosamente en: {ruta_salida}")
    except Exception as e:
        raise Exception(f"Error al guardar el archivo: {e}")


if __name__ == "__main__":
    try:
        # Ruta de entrada y salida
        ruta_archivo = "planilla_iva.xlsx"
        ruta_salida = "calculo_iva.xlsx"

        # Leer y procesar la planilla
        iva_df = leer_planilla_iva(ruta_archivo)
        iva_debito, iva_credito, iva_a_pagar = calcular_iva(iva_df)

        # Guardar los resultados
        guardar_resultados(iva_df, iva_a_pagar, ruta_salida)
    except Exception as e:
        print(f"Error en el proceso: {e}")
