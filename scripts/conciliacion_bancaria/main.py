"""
Conciliación Bancaria:
- Detectar diferencias entre el libro contable y el estado de cuenta bancario.
- Identificar transacciones pendientes o errores.
"""

import pandas as pd


# Leer los registros contables y el estado de cuenta bancario
contable_df = pd.read_excel("libro_contable.xlsx")
bancario_df = pd.read_excel("estado_bancario.xlsx")

# Conciliar usando el monto y la fecha
conciliacion = pd.merge(
    contable_df,
    bancario_df,
    on=["Monto", "Fecha"],
    how="outer",
    indicator=True,
)

# Filtrar las diferencias
no_conciliadas = conciliacion[conciliacion["_merge"] != "both"]

# Guardar las diferencias
no_conciliadas.to_excel("diferencias_conciliacion.xlsx", index=False)
print("Conciliación completada. Diferencias guardadas.")
