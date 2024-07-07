import pandas as pd
import json
import logging
from src.config import query, eng, path_output

logging.basicConfig(format="%(asctime)s - %(filename)s - %(message)s", level=logging.INFO)


def read_from_database(query):
    try:
        logging.info(f'Getting data from database {query}')
        data = pd.read_sql(query, eng)
        logging.info(f'Data retrived from database {query}')
        return data
    except Exception:
        logging.error(f'Could not get the data from {query}')
        raise Exception(f'Could not get the data from {query}')


def data_to_json(df, path):
    try:
        logging.info('Transforming dataframe to json format')
        dict_data = dict(zip(df['country'], df['amount_people']))
        logging.info(f'Json: {dict_data}')
        with open(path, 'w') as json_file:
            json.dump(dict_data, json_file)
        logging.info(f'Json file saved to: {path}')
    except Exception:
        logging.error('Error Tranforming dataframe to json format')
        raise Exception('Error Tranforming dataframe to json format')


def main():
    data = read_from_database(query)
    data_to_json(data, path_output)


if __name__ == "__main__":
    main()
