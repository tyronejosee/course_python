"""
Script de Pokemon

https://pokeapi.co/
"""

import requests
from requests.exceptions import RequestException
import pandas as pd


def obtener_datos_pokemon(id_o_nombre):
    """Obtiene datos de un Pokémon desde la PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{id_o_nombre}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except RequestException as e:
        print(f"Error al obtener datos del Pokémon: {e}")
        return None


def crear_dataframe_pokemon(datos_pokemon):
    """Crea un DataFrame de pandas con los datos de los Pokémon."""
    lista_pokemon = []
    for pokemon in datos_pokemon:
        if pokemon:
            tipos = ", ".join([tipo["type"]["name"] for tipo in pokemon["types"]])
            habilidades = ", ".join(
                [habilidad["ability"]["name"] for habilidad in pokemon["abilities"]]
            )
            pokemon_data = {
                "ID": pokemon["id"],
                "Nombre": pokemon["name"],
                "Tipos": tipos,
                "Habilidades": habilidades,
            }
            lista_pokemon.append(pokemon_data)
    return pd.DataFrame(lista_pokemon)


def guardar_en_excel(df_pokemon, nombre_archivo="pokemon_data.xlsx"):
    """Guarda el DataFrame en un archivo Excel."""
    try:
        df_pokemon.to_excel(
            nombre_archivo, index=False
        )  # index=False para no guardar el índice del DataFrame
        print(f"Datos guardados en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")


def main():
    """Función principal para obtener y guardar datos de Pokémon."""
    num_pokemon = 20
    datos_pokemon = []

    for i in range(1, num_pokemon + 1):
        datos = obtener_datos_pokemon(i)
        datos_pokemon.append(datos)

    df_pokemon = crear_dataframe_pokemon(datos_pokemon)

    if not df_pokemon.empty:  # Verifica que el dataframe no este vacio
        guardar_en_excel(df_pokemon)
    else:
        print("No se pudieron obtener datos para crear el DataFrame.")


if __name__ == "__main__":
    main()
