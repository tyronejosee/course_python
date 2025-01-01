import pandas as pd


def crear_datos_ejemplo():
    """Crea un DataFrame con datos de ejemplo para el estado de resultados."""
    datos = {
        "Concepto": [
            "Ventas",
            "Otros Ingresos",
            "Costo de Ventas",
            "Sueldos",
            "Gastos Administrativos",
        ],
        "Tipo": [
            "Ingreso",
            "Ingreso",
            "Egreso",
            "Egreso",
            "Egreso",
        ],
        "Monto": [
            5000000,
            500000,
            2000000,
            1200000,
            300000,
        ],
    }
    return pd.DataFrame(datos)


def calcular_totales(resultados_df):
    """Calcula los totales de ingresos, egresos y utilidad neta."""
    ingresos = resultados_df.loc[resultados_df["Tipo"] == "Ingreso", "Monto"].sum()
    egresos = resultados_df.loc[resultados_df["Tipo"] == "Egreso", "Monto"].sum()
    utilidad_neta = ingresos - egresos
    return ingresos, egresos, utilidad_neta


def guardar_estado_resultados(
    resultados_df, ingresos, egresos, utilidad_neta, nombre_archivo
):
    """Guarda el estado de resultados en un archivo Excel, incluyendo totales calculados."""
    resultados_df.loc[len(resultados_df)] = ["Total Ingresos", "Ingreso", ingresos]
    resultados_df.loc[len(resultados_df)] = ["Total Egresos", "Egreso", egresos]
    resultados_df.loc[len(resultados_df)] = [
        "Utilidad Neta",
        "Resultado",
        utilidad_neta,
    ]
    resultados_df.to_excel(nombre_archivo, index=False)


def main():
    """Función principal para generar el estado de resultados."""
    # Crear datos de ejemplo
    # TODO: alimentar desde un excel (Balance general)
    resultados_df = crear_datos_ejemplo()

    # Calcular totales
    ingresos, egresos, utilidad_neta = calcular_totales(resultados_df)

    # Guardar el estado de resultados
    guardar_estado_resultados(
        resultados_df,
        ingresos,
        egresos,
        utilidad_neta,
        "estado_resultados.xlsx",
    )

    print(
        f"Ingresos: {ingresos}, Egresos: {egresos}, Utilidad Neta: {utilidad_neta}",
    )


if __name__ == "__main__":
    main()
