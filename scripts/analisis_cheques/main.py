import os
import shutil

import pandas as pd

import constants as cf


def split_excel(input_file, separator) -> list[pd.DataFrame]:
    os.makedirs("docs", exist_ok=True)
    df: pd.DataFrame = pd.read_excel(
        input_file,
        sheet_name=cf.SHEET_NAME,
        header=None,
    )
    df["group"] = (df[0] == separator).cumsum()
    combined_data: list[pd.DataFrame] = []

    for _, data in df.groupby("group"):
        filtered_data: pd.DataFrame = data[data[0] != separator]
        if (
            not filtered_data.empty
            and str(filtered_data.iloc[0, 0]).strip() == "Código:"
        ):
            date_columns: list[int] = [2, 3]
            for col in date_columns:
                filtered_data.loc[:, col] = pd.to_datetime(
                    filtered_data[col],
                    format="%m/%d/%Y",
                    errors="coerce",
                ).dt.strftime("%d-%m-%Y")
            combined_data.append(filtered_data)
    return combined_data


def filter_and_modify_data(df) -> pd.DataFrame:
    filtered_df = df[~df[0].astype(str).str.contains("TOTAL", na=False)]
    filtered_df = filtered_df[
        filtered_df[0].astype(str).str.contains(r"CH|DP", na=False)
    ]
    code: int = df.iloc[0, 1]
    name: str = df.iloc[0, 4]
    filtered_df[0] = code
    filtered_df[1] = name
    filtered_df.drop(columns=[6, 7, 8, 9], inplace=True)
    filtered_df[10] = (
        pd.to_numeric(filtered_df[10], errors="coerce").fillna(0)
        + pd.to_numeric(filtered_df[11], errors="coerce").fillna(0) * -1
    )
    filtered_df.drop(columns=[11, 12], inplace=True)
    filtered_df.reset_index(drop=True, inplace=True)
    filtered_df: pd.DataFrame = filtered_df.drop(index=0)
    return filtered_df


def process_files(input_file, separator, output_file) -> None:
    combined_data: list[pd.DataFrame] = split_excel(input_file, separator)
    if not combined_data:
        print("No data generated. Ending process.")
        return
    modified_data: list[pd.DataFrame] = [
        filter_and_modify_data(df) for df in combined_data
    ]
    final_df: pd.DataFrame = pd.concat(modified_data, ignore_index=True)
    final_df.to_excel(output_file, index=False, header=False)
    clean_up()
    print("Task completed! 🎉")


def clean_up() -> None:
    if os.path.exists("docs"):
        shutil.rmtree("docs")


if __name__ == "__main__":
    process_files(cf.INPUT_FILE, cf.SEPARATOR, cf.OUTPUT_FILE)
