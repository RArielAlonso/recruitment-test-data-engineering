import pandas as pd
from src.config import query, eng, path_output


def read_from_database(query):
    data = pd.read_sql(query, eng)
    return data


def data_to_json(df, path):
    print(df.to_dict())
    df.to_json(path, orient='values')


def main():
    data = read_from_database(query)
    data_to_json(data, path_output)


if __name__ == "__main__":
    main()
