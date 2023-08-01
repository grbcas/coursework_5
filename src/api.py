import requests
import os
import json


class ParserHH:

	def __init__(self, keyword='python'):
		# self.employers = employers
		self.keyword = keyword
		self.api_url = f'https://api.hh.ru/vacancies?text={self.keyword}'
		self.params = {
			"per_page": 20,
			"page": 0,
			"archived": False
		}
		self.header = {"User_Agent": "HHScalperApp 1.0"}
		self.vacancies = []

	def get_vacancy(self):
		"""
		Load vacancies
		:return:
		"""

		hh_vacancies = []
		hh_data = requests.get(self.api_url, headers=self.header, params=self.params).json()

		for vacancy in hh_data['items']:
			try:
				keys_vacancy = {
					'vacancy_id': vacancy['id'],
					'profession': vacancy['name'],
					'salary': vacancy.get('salary').get('from', 0),
					'link': vacancy['alternate_url'],
					'currency': vacancy['salary']["currency"],
					'employer_id': vacancy['employer']['id'],
					'employer_name': vacancy['employer']['name']
				}
			except AttributeError:
				keys_vacancy = {
					'vacancy_id': vacancy['id'],
					'profession': vacancy['name'],
					'salary': 0,
					'link': vacancy['alternate_url'],
					'currency': 'RUB',
					'employer_id': vacancy['employer']['id'],
					'employer_name': vacancy['employer']['name']
				}

			hh_vacancies.append(keys_vacancy)

		return hh_vacancies


if __name__ == '__main__':
	v = ParserHH()
	res = v.get_vacancy()
	print(res)
