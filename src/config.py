from sqlalchemy import create_engine

con_str = "mysql+pymysql://codetest:swordfish@database:3306/codetest"

path_people = 'data/people.csv'
path_places = 'data/places.csv'
path_output = '/data/summary_output.json'

parse_dates = ['date_of_birth']

eng = create_engine(con_str)

query = """
select country,count(*) as amount_people from people p join places pl on pl.place_id=p.place_id group by country;
"""
