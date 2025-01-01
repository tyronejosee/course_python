"""
Libro Mayor:
- Generar automáticamente el libro mayor agrupando
  las transacciones por cuenta contable.
"""

import pandas as pd

# Crear un DataFrame simulando un libro diario con datos ficticios
data = {
    "Fecha": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
    "Cuenta Contable": ["Caja", "Bancos", "Clientes", "Proveedores"],
    "Debe": [1000, 0, 500, 0],
    "Haber": [0, 500, 0, 200],
}
diario_df = pd.DataFrame(data)

# Crear el libro mayor a partir del libro diario
mayor_df = (
    diario_df.groupby("Cuenta Contable")
    .agg({"Debe": "sum", "Haber": "sum"})
    .reset_index()
)

# Calcular el saldo por cuenta
mayor_df["Saldo"] = mayor_df["Debe"] - mayor_df["Haber"]

# Guardar el libro mayor en formato Excel
output_path = "libro_mayor.xlsx"
mayor_df.to_excel(output_path, index=False)

print("Libro mayor generado exitosamente en el archivo:", output_path)
