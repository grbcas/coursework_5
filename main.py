from src.config import config
from src.api import ParserHH
from src.db_utils import create_db, create_tables, save_data_to_db
from src.dbmanager import DBManager
from src.vacancy import Vacancy
import json
from pathlib import Path

def main():
    param_create_db = config()

    create_db(param_create_db)

    params = config()
    create_tables(params)

    path = Path(Path(__file__).parent, 'employers.txt')
    with open(path, encoding='utf8') as json_file:
        employers = json.load(json_file)

    hh_data = []
    for employer_name, employer_id in employers.items():
        vacancy = ParserHH(employer_id).get_vacancy()
        hh_data.extend(vacancy)

    vacancies = []
    for i_vacancy in hh_data:
        vacancy_id = i_vacancy['vacancy_id']
        profession = i_vacancy['profession']
        salary = i_vacancy['salary']
        link = i_vacancy['link']
        currency = i_vacancy['currency']
        employer_id = i_vacancy['employer_id']
        employer_name = i_vacancy['employer_name']
        vacancies.append(Vacancy(vacancy_id, profession, salary, link, currency, employer_id, employer_name))

    vacancies_to_db = []
    for i_vacancy in vacancies:
        vacancies_to_db.append(i_vacancy.__dict__)

    # print(vacancies_to_db)
    save_data_to_db(vacancies_to_db, params)

    d = DBManager(params)
    r1 = d.get_companies_and_vacancies_count()
    r2 = d.get_all_vacancies()
    r3 = d.get_avg_salary()
    r4 = d.get_vacancies_with_higher_salary()

    print('get_companies_and_vacancies_count:')
    print(*r1)
    print('get_all_vacancies:')
    print(*r2)
    print('get_avg_salary:')
    print(*r3)
    print('get_vacancies_with_higher_salary:')
    print(*r4)
    print('get_vacancies_with_keyword:')
    keyword = input(f'enter a keyword to search for, e.g. (Lead / Senior / middle / junior) >>> ')
    r5 = d.get_vacancies_with_keyword(keyword)
    print(*r5)
    d.connect().close()


if __name__ == '__main__':
    main()
