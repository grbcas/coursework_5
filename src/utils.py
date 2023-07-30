"""
Функция для взаимодействия с пользователем.
Функция должна взаимодействовать с пользователем через консоль:
 с каких платформ он хочет получить вакансии,
 ввести поисковый запрос,
 получить топ N вакансий по зарплате,
 получить вакансии в отсортированном виде,
 получить вакансии, в описании которых есть определенные ключевые слова, например "postgres" и т.п.
"""
from sys import stdin


def interact_user(_in=stdin):
    """
    Choose hr_platform,
    enter search_keyword,
    set number of vacancies to load
    :param _in:
    :return:
    """
    hr_platform = {0: 'HeadHunter', 1: 'SuperJob'}
    [print(key, ':', value, end="\n") for key, value in hr_platform.items()]
    while True:
        try:
            print('enter hr_platform id>')
            input_ = _in.readline()
            if int(input_) in range(0, 2):
                hr_id = int(input_)
                print(hr_platform.get(hr_id))
                break
            else:
                raise ValueError
        except ValueError:
            print('enter number in range(0, 1)')

    print('search_keyword')
    search_keyword = _in.readline().strip()

    while True:
        try:
            print('input enter top_n_vacancies >')
            input_ = _in.readline()
            if int(input_) in range(20):
                top_n_vacancies = int(input_)
                print('top_n_vacancies =', top_n_vacancies)
                break
            else:
                raise ValueError
        except ValueError:
            print(f'enter number in range(1, {20})')

    save_option = 0
    while True:
        try:
            print('Choose options for data: save to file: 0, save and display: 1')
            input_ = _in.readline()
            if int(input_) in range(0, 2):
                save_option = int(input_)
                break
            else:
                raise ValueError
        except ValueError:
            print('enter number in range(0, 1)')

    user_input = {'hr_platform': hr_platform.get(hr_id),
                  'keyword': search_keyword,
                  'top_n_vacancies': top_n_vacancies,
                  'save_option': save_option}

    return user_input
