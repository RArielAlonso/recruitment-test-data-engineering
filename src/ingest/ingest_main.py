import pandas as pd
import logging
from src.config import path_places, path_people, parse_dates, eng

logging.basicConfig(format="%(asctime)s - %(filename)s - %(message)s", level=logging.INFO)


def read_csv(path, parse_dates=[]):
    try:
        logging.info(f'Reading csv from {path}')
        data = pd.read_csv(path, encoding='UTF-8', parse_dates=parse_dates)
        logging.info(f'Csv succesfully read from {path}')
        return data
    except FileNotFoundError:
        logging.error(f'Csv file not found in {path}')
        raise FileNotFoundError(f'Csv file not found in {path}',)
    except Exception as e:
        logging.error(f'Error reading csv in {path}')
        logging.error(f"{e}")
        raise Exception(f'Error reading csv in {path}')


def transform_places(df):
    logging.info('Transforming Places dataframe')
    df.reset_index(inplace=True)
    df.columns = ['place_id', 'city', 'county', 'country']
    df.loc[:, 'place_id'] = df.loc[:, 'place_id']+1
    logging.info('Finished transforming Places dataframe')
    return df


def transform_people(df_people, df_places):
    logging.info('Transforming People dataframe')
    df_people.columns = ['given_name', 'family_name', 'date_of_birth', 'place_id']
    df_people = df_people.merge(df_places, how='inner', left_on='place_id', right_on='city').rename({'place_id_y': 'place_id'}, axis=1)
    df_people = df_people[['given_name', 'family_name', 'date_of_birth', 'place_id']]
    logging.info('Finished transforming People dataframe')
    return df_people


def load_to_database(df, table_name):
    try:
        logging.info(f'Loading data to database in {table_name}')
        df.to_sql(table_name, con=eng, if_exists='append', index=False)
        logging.info(f'Data loaded succesfully to database in {table_name}')
    except Exception:
        logging.error(f'Could not complete the loading to the database in {table_name}')
        raise Exception(f'Could not complete the loading to the database in {table_name}')


def main():
    data_places = read_csv(path_places)
    data_people = read_csv(path_people, parse_dates=parse_dates)
    data_places = transform_places(data_places)
    data_people = transform_people(data_people, data_places)
    load_to_database(data_places, 'places')
    load_to_database(data_people, 'people')


if __name__ == "__main__":
    main()
