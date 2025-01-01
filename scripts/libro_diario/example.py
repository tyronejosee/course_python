"""
Libro Diario:
- Automatizar la generación y verificación de balances entre `Debe` y `Haber`.
- Cargar o guardar los datos desde/para Excel.
"""

import pandas as pd


# Leer el libro diario desde Excel
diario_df = pd.read_excel("libro_diario.xlsx")

# Verificar que el balance esté cuadrado (Debe == Haber por asiento)
diario_df["Balance"] = diario_df["Debe"] - diario_df["Haber"]
balance_cuadrado = diario_df.groupby("Número de Asiento")["Balance"].sum().eq(0).all()

if balance_cuadrado:
    print("El libro diario está cuadrado.")
else:
    print("Hay desbalances en el libro diario.")

# Guardar los resultados en un nuevo archivo
diario_df.to_excel("libro_diario_verificado.xlsx", index=False)
