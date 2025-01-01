"""
Flujo de Caja:
- Automatizar la suma acumulativa de ingresos y egresos
  para calcular el saldo diario.
"""

import pandas as pd


# Leer flujo de caja desde Excel
flujo_df = pd.read_excel("flujo_caja.xlsx")

# Calcular saldo acumulado
flujo_df["Saldo"] = (
    flujo_df["Ingresos (CLP)"].fillna(0).cumsum()
    - flujo_df["Egresos (CLP)"].fillna(0).cumsum()
)

# Guardar el flujo actualizado
flujo_df.to_excel("flujo_caja_actualizado.xlsx", index=False)
print("Flujo de caja actualizado y guardado.")
