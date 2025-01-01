import pandas as pd

# Crear un DataFrame simulando un libro diario con datos ficticios
data = {
    "Fecha": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
    "Cuenta Contable": ["Caja", "Bancos", "Clientes", "Proveedores"],
    "Debe": [1000, 0, 500, 0],
    "Haber": [0, 500, 0, 200],
}
diario_df = pd.DataFrame(data)


# Validar datos antes de procesar
def validar_datos(df):
    if df.isnull().values.any():
        raise ValueError(
            "El libro diario contiene valores nulos. Por favor, revise los datos."
        )
    if not all(
        col in df.columns for col in ["Fecha", "Cuenta Contable", "Debe", "Haber"]
    ):
        raise ValueError(
            "El libro diario debe contener las columnas 'Fecha', 'Cuenta Contable', 'Debe' y 'Haber'."
        )
    print("Datos validados correctamente.")


# Crear el libro mayor a partir del libro diario
def generar_libro_mayor(diario):
    validar_datos(diario)
    mayor_df = (
        diario.groupby("Cuenta Contable")
        .agg({"Debe": "sum", "Haber": "sum"})
        .reset_index()
    )
    # Calcular el saldo por cuenta
    mayor_df["Saldo"] = mayor_df["Debe"] - mayor_df["Haber"]
    return mayor_df


# Guardar el libro mayor en formato Excel
def guardar_libro_mayor(df, ruta):
    try:
        df.to_excel(ruta, index=False, engine="openpyxl")
        print("Libro mayor generado exitosamente en el archivo:", ruta)
    except Exception as e:
        print("Error al guardar el archivo:", e)


if __name__ == "__main__":
    try:
        # Generar el libro mayor
        libro_mayor_df = generar_libro_mayor(diario_df)
        # Ruta de salida
        output_path = "libro_mayor.xlsx"
        # Guardar el libro mayor
        guardar_libro_mayor(libro_mayor_df, output_path)
    except Exception as e:
        print("Error durante la generación del libro mayor:", e)
