"""
Generación Automática de Reportes:
- Crear gráficos y resúmenes a partir de los datos.
- Guardar el reporte como un archivo Excel o PDF.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# Supongamos que ya tenemos un DataFrame `flujo_df` con los datos de flujo de caja
# Crear un DataFrame simulado con datos de ejemplo
data = {
    "Fecha": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Concepto": ["Ingreso", "Egreso", "Ingreso", "Egreso", "Ingreso"],
    "Monto": [100000, 50000, 200000, 30000, 150000],
}
flujo_df = pd.DataFrame(data)

# Generar un resumen de ingresos y egresos
reporte = flujo_df.groupby("Concepto").sum()

# Guardar el resumen como archivo Excel
reporte.to_excel("reporte_resumen.xlsx", index=True)

# Visualizar con gráficos
reporte.plot(
    kind="bar",
    title="Resumen de Ingresos y Egresos",
    color=["green", "red"],
)
plt.xlabel("Concepto")
plt.ylabel("Monto (CLP)")
plt.tight_layout()

# Guardar el gráfico como una imagen PNG
plt.savefig("grafico_ingresos_egresos.png")

# Si se desea guardar el reporte como PDF (requiere ReportLab)
with PdfPages("reporte_completo.pdf") as pdf:
    plt.figure()
    reporte.plot(
        kind="bar",
        title="Resumen de Ingresos y Egresos",
        color=["green", "red"],
    )
    plt.xlabel("Concepto")
    plt.ylabel("Monto (CLP)")
    plt.tight_layout()
    pdf.savefig()  # Guardar gráfico en el PDF
    plt.close()

print("Reporte generado y guardado exitosamente.")
