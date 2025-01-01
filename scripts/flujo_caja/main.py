"""
Flujo de Caja:
- Automatizar la suma acumulativa de ingresos y egresos
  para calcular el saldo diario.
"""

import pandas as pd


def leer_flujo_caja(nombre_archivo):
    """Lee el flujo de caja desde un archivo Excel."""
    return pd.read_excel(nombre_archivo)


def calcular_saldo_acumulado(flujo_df):
    """Calcula el saldo acumulado a partir de los ingresos y egresos."""
    flujo_df["Saldo"] = (
        flujo_df["Ingresos (CLP)"].fillna(0).cumsum()
        - flujo_df["Egresos (CLP)"].fillna(0).cumsum()
    )
    return flujo_df


def guardar_flujo_caja(flujo_df, nombre_archivo):
    """Guarda el flujo de caja actualizado en un archivo Excel."""
    flujo_df.to_excel(nombre_archivo, index=False)


def main():
    """Función principal para automatizar el flujo de caja."""
    # Leer el archivo de flujo de caja
    flujo_df = leer_flujo_caja("flujo_caja.xlsx")

    # Calcular el saldo acumulado
    flujo_actualizado = calcular_saldo_acumulado(flujo_df)

    # Guardar el flujo actualizado
    guardar_flujo_caja(flujo_actualizado, "flujo_caja_actualizado.xlsx")

    print("Flujo de caja actualizado y guardado.")


if __name__ == "__main__":
    main()
