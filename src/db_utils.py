import psycopg2
from src.config import config


def create_db(params: dict):
    """
    creation db: hh
    :param params:
    :return:
    """
    # print(create_db, params)
    params['dbname'] = 'postgres'
    con = psycopg2.connect(**params)
    con.autocommit = True
    with con.cursor() as cur:
        cur.execute(
            """
            DROP database IF EXISTS hh WITH (FORCE);
            """
        )
        cur.execute(
            """
            create database hh
            with
            owner postgres
            tablespace = pg_default
            encoding 'utf-8'
            CONNECTION LIMIT = -1;
            """
        )
    con.close()


def create_tables(params: dict):
    """
    creation tables in db hh
    :param params:
    :return:
    """
    params['dbname'] = 'hh'
    # print(create_tables, params)
    con = psycopg2.connect(**params)
    con.autocommit = True
    with con.cursor() as cur:
        cur.execute(
            """
            create table employers (
            employer_id integer primary key,
            employer_name varchar(100)
            );
            """
        )
        cur.execute(
            """
            create table vacancies (
            vacancy_id integer primary key,
            vacancy_name varchar(100),
            salary integer,
            link varchar(200),
            employer_id integer references employers(employer_id)
            );
            """
        )
    con.close()


def save_data_to_db(data: list[dict[str, any]], params: dict):
    """
    save data in the DB HH,
    :param params:
    :param database_name:
    :param data:
    :return: none
    """
    con = psycopg2.connect(**params)
    # print(save_data_to_db, params)
    with con.cursor() as cur:
        con.autocommit = True
        # get uniq employer_id, employer_name from data
        # ids = set()
        # names = set()
        # for employer in data:
        #     ids.add(employer['employer_id'])
        #     names.add(employer['employer_name'])
        #
        # employers = zip(ids, names)

        # for employer in employers:
        #     cur.execute(
        #         """
        #         insert into employers (employer_id, employer_name)
        #         values(%s, %s);
        #         """,
        #         (int(employer[0]), employer[1])
        #     )

        for employer in data:
            cur.execute(
                """
                insert into employers (employer_id, employer_name)
                values(%s, %s)
                on conflict on constraint employers_pkey do nothing;
                """,
                (int(employer['employer_id']), employer['employer_name'])
            )

        for vacancy in data:
            cur.execute(
                """
                insert into vacancies (vacancy_id, vacancy_name, salary, link, employer_id)
                values(%s, %s, %s, %s, %s);
                """,
                (int(vacancy['vacancy_id']), vacancy['profession'],
                 int(vacancy['_salary']), vacancy['link'], int(vacancy['employer_id']))
            )
    con.close()


if __name__ == '__main__':
    db_params = config()
    create_db(db_params)
    data = [{'vacancy_id': '84201801', 'profession': 'Разработчик python', 'salary': 2500, 'link': 'https://hh.ru/vacancy/84201801', 'currency': 'BYR', 'employer_id': '9417901', 'employer_name': 'Олихвер В. В.'},
            {'vacancy_id': '83618124', 'profession': 'Junior Backend developer (Python)', 'salary': 0, 'link': 'https://hh.ru/vacancy/83618124', 'currency': 'RUB', 'employer_id': '9113528', 'employer_name': 'Effective Mobile'},
            {'vacancy_id': '84180918', 'profession': 'Back-End разработчик', 'salary': 0, 'link': 'https://hh.ru/vacancy/84180918', 'currency': 'RUB', 'employer_id': '4155490', 'employer_name': 'AVR Group'},
            {'vacancy_id': '83902101', 'profession': 'Junior Data Scientist (стажер)', 'salary': 50000, 'link': 'https://hh.ru/vacancy/83902101', 'currency': 'RUR', 'employer_id': '4768936', 'employer_name': 'А17'}]
    save_data_to_db(data, db_params)

