
-- `get_companies_and_vacancies_count()`:
-- получает список всех компаний и количество вакансий у каждой компании.
select e.employer_name, count(v.vacancy_id)
from vacancies v
join employers e using(employer_id)
group by e.employer_name;


-- get_all_vacancies():
-- получает список всех вакансий с указанием названия компании,
-- названия вакансии и зарплаты и ссылки на вакансию.
select e.employer_name, v.vacancy_name, v.salary, v.link
from vacancies v
join employers e using(employer_id);

-- `get_avg_salary()`:
-- получает среднюю зарплату по вакансиям.
select round(avg(v.salary)::numeric, 2)
from vacancies v
where v.salary > 0;

-- `get_vacancies_with_higher_salary()`:
-- получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
select v.vacancy_id, v.vacancy_name, v.salary
from vacancies v
where v.salary >
(select round(avg(v.salary)::numeric, 2)
from vacancies v
where v.salary > 0);

-- `get_vacancies_with_keyword()`:
-- получает список всех вакансий with keyword
select v.vacancy_id, v.vacancy_name
from vacancies v
where v.vacancy_name ilike '%python%';
