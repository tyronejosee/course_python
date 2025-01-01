"""
Generación Automática de Reportes:
- Crear gráficos y resúmenes a partir de los datos.
- Guardar el reporte como un archivo Excel o PDF.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def generar_datos_ejemplo():
    """Crea un DataFrame de ejemplo con datos simulados."""
    data = {
        "Fecha": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
        "Concepto": ["Ingreso", "Egreso", "Ingreso", "Egreso", "Ingreso"],
        "Monto": [100000, 50000, 200000, 30000, 150000],
    }
    return pd.DataFrame(data)


def generar_resumen(flujo_df):
    """Genera un resumen agrupando por concepto."""
    return flujo_df.groupby("Concepto")["Monto"].sum()


def guardar_resumen_excel(resumen, nombre_archivo):
    """Guarda el resumen en un archivo Excel."""
    resumen.to_excel(nombre_archivo)


def crear_grafico(resumen, nombre_archivo):
    """Crea y guarda un gráfico de barras del resumen."""
    colores = [
        "green" if concepto == "Ingreso" else "red" for concepto in resumen.index
    ]
    resumen.plot(
        kind="bar",
        title="Resumen de Ingresos y Egresos",
        color=colores,
    )
    plt.xlabel("Concepto")
    plt.ylabel("Monto (CLP)")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()


def guardar_reporte_pdf(resumen, nombre_archivo):
    """Guarda el resumen y el gráfico en un archivo PDF."""
    with PdfPages(nombre_archivo) as pdf:
        plt.figure()
        colores = [
            "green" if concepto == "Ingreso" else "red" for concepto in resumen.index
        ]
        resumen.plot(kind="bar", title="Resumen de Ingresos y Egresos", color=colores)
        plt.xlabel("Concepto")
        plt.ylabel("Monto (CLP)")
        plt.tight_layout()
        pdf.savefig()
        plt.close()


def main():
    """Función principal para generar el reporte."""
    flujo_df = generar_datos_ejemplo()

    # Generar el resumen
    resumen = generar_resumen(flujo_df)

    # Guardar el resumen como Excel
    guardar_resumen_excel(resumen, "reporte_resumen.xlsx")

    # Crear y guardar el gráfico
    crear_grafico(resumen, "grafico_ingresos_egresos.png")

    # Guardar el reporte completo como PDF
    guardar_reporte_pdf(resumen, "reporte_completo.pdf")

    print("Reporte generado y guardado exitosamente.")


if __name__ == "__main__":
    main()
