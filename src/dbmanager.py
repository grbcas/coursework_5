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


class DBManager:
    def __init__(self, params: dict):
        self.params = params

    def connect(self):
        try:
            conn = psycopg2.connect(**self.params)
            return conn
        except Exception as e:
            print(e)
        # finally:
        #     conn.close()

    def get_companies_and_vacancies_count(self):
        with self.connect().cursor() as cur:
            postgres_select_query = \
                """
                select e.employer_name, count(v.vacancy_id) 
                from vacancies v 
                join employers e using(employer_id)
                group by e.employer_name;           
                """

            cur.execute(postgres_select_query)
            select_output = cur.fetchall()

        self.connect().commit()
        return select_output

    def get_all_vacancies(self):
        with self.connect().cursor() as cur:
            postgres_select_query = \
                """
                select e.employer_name, v.vacancy_name, v.salary, v.link 
                from vacancies v
                join employers e using(employer_id);          
                """

            cur.execute(postgres_select_query)
            select_output = cur.fetchall()

        self.connect().commit()
        return select_output

    def get_avg_salary(self):
        with self.connect().cursor() as cur:
            postgres_select_query = \
                """
                select round(avg(v.salary)::numeric, 2) 
                from vacancies v
                where v.salary > 0;         
                """

            cur.execute(postgres_select_query)
            select_output = cur.fetchall()

        self.connect().commit()
        return select_output

    def get_vacancies_with_higher_salary(self):
        with self.connect().cursor() as cur:
            postgres_select_query = \
                """
                select v.vacancy_id, v.vacancy_name, v.salary 
                from vacancies v
                where v.salary > 
                (select round(avg(v.salary)::numeric, 2) 
                from vacancies v
                where v.salary > 0);       
                """

            cur.execute(postgres_select_query)
            select_output = cur.fetchall()

        self.connect().commit()
        return select_output

    def get_vacancies_with_keyword(self, keyword):
        with self.connect().cursor() as cur:
            postgres_select_query = \
                f"""
                select v.vacancy_id, v.vacancy_name
                from vacancies v
                where v.vacancy_name ilike '%{keyword}%';      
                """

            cur.execute(postgres_select_query)
            select_output = cur.fetchall()

        self.connect().commit()
        return select_output
