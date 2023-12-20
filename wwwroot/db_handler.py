from config import Config
import pandas as pd
import os


config = Config()


def get_country_names():
    column_name = "name"
    csv_filepath = config.db_path
    df = pd.read_csv(csv_filepath, sep=";", encoding='utf-8')

    if column_name in df.columns:
        column_data = df[column_name].tolist()
        return column_data
    else:
        return None


def get_country_names_by_input(input_string):
    csv_filepath = config.db_path
    df = pd.read_csv(csv_filepath, sep=";", encoding='utf-8')
    filtered_df = df[df['name'].str.contains(input_string)]
    return filtered_df


def get_data_by_country_name(full_name):
    csv_filepath = config.db_path
    df = pd.read_csv(csv_filepath, sep=";", encoding='utf-8')
    row = df[df['name'] == full_name]
    row = row.fillna('')
    if not row.empty:

        data = row.to_dict(orient='records')
        print(data)
        print('123')
        return data[0]
    return None


def find_file_by_extension(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                return file

