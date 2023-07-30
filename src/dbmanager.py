"""
методы:
- `get_companies_and_vacancies_count()`:
получает список всех компаний и количество вакансий у каждой компании.
- `get_all_vacancies()`:
получает список всех вакансий с указанием названия компании,
 названия вакансии и зарплаты и ссылки на вакансию.
- `get_avg_salary()`:
получает среднюю зарплату по вакансиям.
- `get_vacancies_with_higher_salary()`:
получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
- `get_vacancies_with_keyword()`:
получает список всех вакансий,
 в названии которых содержатся переданные в метод слова, например “python”.
"""

import psycopg2
from config import config


class DBManager:
    def __init__(self, params: dict):
        self.params = params

    def connect(self):


    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass