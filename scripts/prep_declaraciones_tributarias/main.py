"""
Preparación de Declaraciones Tributarias:
- Calcular IVA, PPM, e impuesto a la renta.
- Generar un archivo prellenado para el Formulario 29 o 22.
"""

import pandas as pd
from datetime import datetime


def calcular_iva(ventas, compras):
    """Calcula el IVA a pagar o saldo a favor."""
    iva_ventas = ventas * 0.19
    iva_compras = compras * 0.19
    iva_pagar = iva_ventas - iva_compras
    return iva_pagar


def calcular_ppm(ingresos_brutos):
    """Calcula el Pago Provisional Mensual (PPM)."""
    ppm = ingresos_brutos * 0.003
    return ppm


def calcular_impuesto_renta(utilidades):
    """Calcula el impuesto a la renta anual (27% para empresas en Chile)."""
    impuesto_renta = utilidades * 0.27
    return impuesto_renta


def generar_formulario(tipo_formulario, datos):
    """Genera un archivo CSV con los datos del formulario especificado."""
    nombre_archivo = (
        f"Formulario_{tipo_formulario}_{datetime.now().strftime('%Y%m%d')}.csv"
    )
    datos.to_csv(nombre_archivo, index=False, encoding="utf-8-sig")
    print(f"Formulario {tipo_formulario} generado: {nombre_archivo}")


# Solicitar datos al usuario
ventas = float(input("Ingrese el monto total de ventas (sin IVA): "))
compras = float(input("Ingrese el monto total de compras (sin IVA): "))
ingresos_brutos = float(input("Ingrese el monto total de ingresos brutos: "))
utilidades = float(input("Ingrese el monto total de utilidades anuales: "))

# Calcular impuestos
iva_pagar = calcular_iva(ventas, compras)
ppm = calcular_ppm(ingresos_brutos)
impuesto_renta = calcular_impuesto_renta(utilidades)

# Preparar datos para el formulario 29
formulario_29 = pd.DataFrame(
    {
        "Concepto": ["IVA Ventas", "IVA Compras", "IVA a Pagar", "PPM"],
        "Monto": [ventas * 0.19, compras * 0.19, iva_pagar, ppm],
    }
)

generar_formulario(29, formulario_29)

# Preparar datos para el formulario 22
formulario_22 = pd.DataFrame(
    {
        "Concepto": ["Utilidades", "Impuesto a la Renta"],
        "Monto": [utilidades, impuesto_renta],
    }
)

generar_formulario(22, formulario_22)

print("Cálculos y generación de formularios completados.")
