from config import config
from src.api import *
from src.db_utils import *

db_params = config()
create_db(db_params)
data = [{'vacancy_id': '84201801', 'profession': 'Разработчик python', 'salary': 2500,
         'link': 'https://hh.ru/vacancy/84201801', 'currency': 'BYR', 'employer_id': '9417901',
         'employer_name': 'Олихвер В. В.'},
        {'vacancy_id': '83618124', 'profession': 'Junior Backend developer (Python)', 'salary': 0,
         'link': 'https://hh.ru/vacancy/83618124', 'currency': 'RUB', 'employer_id': '9113528',
         'employer_name': 'Effective Mobile'},
        {'vacancy_id': '84180918', 'profession': 'Back-End разработчик', 'salary': 0,
         'link': 'https://hh.ru/vacancy/84180918', 'currency': 'RUB', 'employer_id': '4155490',
         'employer_name': 'AVR Group'},
        {'vacancy_id': '83902101', 'profession': 'Junior Data Scientist (стажер)', 'salary': 50000,
         'link': 'https://hh.ru/vacancy/83902101', 'currency': 'RUR', 'employer_id': '4768936', 'employer_name': 'А17'}]
save_data_to_db(data, db_params)
for employer in data:
    print(int(employer['employer_id']), employer['employer_name'])