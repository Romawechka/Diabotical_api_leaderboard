# Diabotical_api_leaderboard
+ Для того, чтобы установить все необходимые библиотеки воспользуйтесь командой: **pip install -r requirements.txt**
+ Необходимо вызвать файл в командной строке командой **python leaderboard.py** и указать аргументы для выборки (аргумент mode является обязательным,
при запуске без него программа подскажет какие режимы можно запросить)

```
    leaderboard.py [-h] [--mode MODE] [--count COUNT] [--user_id USER_ID] [--country COUNTRY]

    Diabotical api

    optional arguments:
      -h, --help         show this help message and exit
      --mode MODE        Input game mode
      --count COUNT      Input count users
      --user_id USER_ID  Input id users
      --country COUNTRY  Input country users

```
+ Пример вызова **python leaderboard.py --mode r_macguffin --count 2**

```
{
  "leaderboard": [
    {
      "0": [
        {
          "name": "enesy",
          "country": "dk",
          "match_type": 2,
          "rating": "2246",
          "rank_tier": 40,
          "rank_position": 1,
          "match_count": 48,
          "match_wins": 42
        }
      ]
    },
    {
      "1": [
        {
          "name": "Cookk1",
          "country": "",
          "match_type": 2,
          "rating": "2216",
          "rank_tier": 40,
          "rank_position": 2,
          "match_count": 34,
          "match_wins": 30
        }
      ]
    }
  ]
}
```
+ Пример вызова **python leaderboard.py --mode r_macguffin --count 2 --country ru**
```
Игроков из страны: ru в игре с модом r_macguffin - 0 человек
```
+ Пример вызова **python leaderboard.py --mode r_macguffin --user_id aee1fba486c54d1d8600b3c82c9264d7**
```
{
  "leaderboard": [
    {
      "1": [
        {
          "name": "Cookk1",
          "country": "",
          "match_type": 2,
          "rating": "2216",
          "rank_tier": 40,
          "rank_position": 2,
          "match_count": 34,
          "match_wins": 30
        }
      ]
    }
  ]
}
```
