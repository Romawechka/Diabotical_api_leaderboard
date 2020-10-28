"""
Author: https://github.com/Romawechka
Python version 3.8.5
"""

import argparse
import time
import requests
import json


def diabotical_parser(mode, count, user_id, country):
    """
    :param mode: Отвечает за ввод мода игры
    :param count: Отвечает за колличество игроков для вывода
        default: 20
    :param user_id: Отвечает за ввод id игрока
    :param country: Отвечает за ввывод играков из конкретной страны
    """

    Error_massage1 = False
    Error_massage = False

    if not mode:
        Error = '\nПараметр mode должны быть обязательно указан.\nСписок доступных mode: [r_macguffin, r_wo,' \
                ' r_rocket_arena_2, r_shaft_arena_1, r_ca_2, r_ca_1]\n'
        print(Error)
        return Error

    _mode = mode
    mode = 'mode=' + mode + '&'

    page = 0
    if count is None:
        count = 20
    elif count <= 0:
        Error_massage = '\ncount не может быть меньше 0 или равняться ему,' \
                        ' попробуйте другое положительное значение, например 1\n'
        print(Error_massage)
        return Error_massage

    # Создаем пустой файл для вывода
    mega = json.loads('{"leaderboard": []}')

    # Переменная подсчета игроков
    count_user = 0
    country_count = 0

    finish = True
    while finish:

        try:
            req = requests.get(f'https://www.diabotical.com/api/v0/stats/leaderboard?{mode}offset={page}')

            # http ошибки сервера/клиента
            if req.status_code >= 500:
                print('\nApi сейчас недоступно\n')
                break
            elif req.status_code >= 400:
                print('\nПохоже неправильно заданы параметры запроса\n')
                break

        except Exception:
            print('\nПроблемы с соединением. Проверьте свой интернет, или возможно'
                  ' в данный момент сервис API недоступен\n')
            break

        my_json = req.content.decode('utf8')
        data = json.loads(my_json)

        # Проверяем на ошибки (можно было бы и через try/exept но тогда необходимо было бы решать путанницу)
        if not data['leaderboard'] and page != 0:
            Error_massage1 = True
            break
        elif not data['leaderboard'] and page == 0:
            Error_massage = True
            break

        # итерация по списку пользователей
        for el in data['leaderboard']:

            # удаляем запись user_id
            if (el['user_id'] != user_id) and (user_id is not None):
                count_user += 1
                continue
            else:
                el.pop('user_id', None)

            # если не вышли за пределы count
            if count_user <= count - 1:

                # Проверяем собираем ли информацию по стране
                if not country:
                    mega['leaderboard'] += [{str(count_user): [el]}]
                elif el['country'] == country:
                    country_count += 1
                count_user += 1

            else:
                finish = False
                break

        page += 20  # смещение
        time.sleep(0.2)  # чтобы не поймать ошибку слишком частых запросов

    # вывод и обработка неккоректных выводов
    if mega['leaderboard']:
        print(json.dumps(mega, indent=2, sort_keys=False))

        if Error_massage1 and (user_id is None):
            print('\nВ игре с данным модом нету столько игроков, все игроки которые есть были выведены\n')

        return [mega, Error_massage1]

    # ситуация когда ненашелся игрок с конкретным id
    elif user_id is not None:
        if count == 0:
            count = 19
        Error_massage = f'\nИгрока с id: {user_id} нету в игре с модом {_mode} среди {count} игроков\n'
        print(Error_massage)
        return Error_massage

    # ситуация с нахождением/отсутствием игроков конкретной страны
    elif country is not None:
        mesaage = f'\nИгроков из страны: {country} в игре с модом {_mode} ' \
                  f'- {country_count} человек\n'
        print(mesaage)
        return mesaage

    elif Error_massage:
        Error_massage = f'\nВ игре нету мода: {_mode}\n'
        print(Error_massage)
        return Error_massage


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Diabotical api')
    parser.add_argument('--mode', type=str, help='Input game mode')
    parser.add_argument('--count', type=int, help='Input count users')
    parser.add_argument('--user_id', type=str, help='Input id users')
    parser.add_argument('--country', type=str, help='Input country users')

    args = parser.parse_args()
    diabotical_parser(mode=args.mode, count=args.count, user_id=args.user_id,
                      country=args.country)
