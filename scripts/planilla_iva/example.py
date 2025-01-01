"""
Planilla de IVA:
- Calcular automáticamente el IVA débito y crédito fiscal,
  y determinar el IVA a pagar.
"""

import pandas as pd

# Leer planilla de IVA desde Excel
iva_df = pd.read_excel("planilla_iva.xlsx")

# Separar débito y crédito fiscal
iva_debito = iva_df.loc[
    iva_df["Tipo de IVA"] == "Débito Fiscal",
    "IVA (19%)",
].sum()
iva_credito = iva_df.loc[
    iva_df["Tipo de IVA"] == "Crédito Fiscal",
    "IVA (19%)",
].sum()

# Calcular el IVA a pagar
iva_a_pagar = iva_debito - iva_credito

print(
    f"IVA Débito: {iva_debito}, IVA Crédito: {iva_credito}, IVA a Pagar: {iva_a_pagar}"
)

# Guardar el cálculo
iva_df["IVA a Pagar"] = iva_a_pagar
iva_df.to_excel("calculo_iva.xlsx", index=False)
