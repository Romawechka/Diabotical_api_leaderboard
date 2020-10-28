import time
import unittest
from leaderboard import diabotical_parser


class Test(unittest.TestCase):

    def test_first(self):
        """Проверка вывода ошибки неверного мода"""
        mode = 'Неверный мод'
        count = None
        user_id = None
        country = None

        Expected = f'\nВ игре нету мода: {mode}\n'

        time.sleep(1)
        self.assertEqual(diabotical_parser(mode, count, user_id, country), Expected)

    def test_second(self):
        """Проверка вывода заданного колличества"""
        mode = 'r_macguffin'
        count = 3
        user_id = None
        country = None

        count_users = 0
        Expected = 3

        time.sleep(1)
        res = diabotical_parser(mode, count, user_id, country)

        for el in res[0]['leaderboard']:
            count_users += 1

        self.assertEqual(count_users, Expected)

    def test_third(self):
        """Проверка вывода сообщения об ошибке, когда count больше чем игроков"""
        mode = 'r_macguffin'
        count = 502
        user_id = None
        country = None

        Expected = True

        time.sleep(1)
        res = diabotical_parser(mode, count, user_id, country)

        self.assertEqual(res[1], Expected)

    def test_fourth(self):
        """Проверка вывода сообщения об ошибке, когда mode не задано"""
        mode = None
        count = None
        user_id = None
        country = None

        Expected = '\nПараметр mode должны быть обязательно указан.\nСписок доступных mode: [r_macguffin, r_wo,' \
                   ' r_rocket_arena_2, r_shaft_arena_1, r_ca_2, r_ca_1]\n'

        time.sleep(1)
        res = diabotical_parser(mode, count, user_id, country)

        self.assertEqual(res, Expected)

    def test_fifth(self):
        """Проверка вывода игрока с конкретным id"""
        mode = 'r_macguffin'
        count = None
        user_id = 'b325363ffe6d46c8840c951b334cc09c'
        country = None

        count_users = 0
        Expected = 1

        time.sleep(1)
        res = diabotical_parser(mode, count, user_id, country)

        for el in res[0]['leaderboard']:
            count_users += 1

        self.assertEqual(res[1], Expected)

    def test_sixth(self):
        """Проверка вывода сообщения об ошибке, когда игрока с конкретным id нету в выборке"""
        mode = 'r_macguffin'
        count = 2
        user_id = '1b9b0f7d3d4c42e59c4e84e55a208023'
        country = None

        Expected = f'\nИгрока с id: {user_id} нету в игре с модом {mode} среди {count} игроков\n'

        time.sleep(1)
        res = diabotical_parser(mode, count, user_id, country)

        self.assertEqual(res, Expected)

    def test_seventh(self):
        """Проверка вывода сообщения об ошибке, когда count <= 0"""
        for i in range(-1, 1):
            mode = 'r_macguffin'
            count = i
            user_id = None
            country = None

            Expected = '\ncount не может быть меньше 0 или равняться ему,' \
                       ' попробуйте другое положительное значение, например 1\n'

            time.sleep(1)
            res = diabotical_parser(mode, count, user_id, country)

            self.assertEqual(res, Expected)

    def test_eighth(self):
        """Проверка вывода сообщения об ошибке, когда игрока с конкретным id нету в выборке"""
        mode = 'r_macguffin'
        count = 2
        user_id = '1b9b0f7d3d4c42e59c4e84e55a208023'
        country = None

        Expected = f'\nИгрока с id: {user_id} нету в игре с модом {mode} среди {count} игроков\n'

        time.sleep(1)
        res = diabotical_parser(mode, count, user_id, country)

        self.assertEqual(res, Expected)

    def test_tenth(self):
        """Проверка вывода колличества игроков из конкретной страны"""
        mode = 'r_macguffin'
        count = None
        user_id = None
        country = 'ru'

        Expected = f'\nИгроков из страны: {country} в игре с модом {mode} ' \
                   f'- 3 человек\n'

        time.sleep(1)
        res = diabotical_parser(mode, count, user_id, country)

        self.assertEqual(res, Expected)


if __name__ == "__main__":
    unittest.main()
