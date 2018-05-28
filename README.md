# Ближайшие бары

Проект создан для определения:
 - самого большого бара, по посадочным местам;
 - самого маленького бара, по посадочным местам;
 - ближайщего бара по заданным координатам.

Данные по барам беруться из файла формата _json_ (скаченного с сайта  [DATA.MOS.RU](http://data.mos.ru/opendata/7710881420-bary)).

_Пример файла находится в репозитории **bars.json**_

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

## Запуск на Linux:

```bash

$ python bars.py [FILEPATH] [LONGTITUDE] [LATITUDE]
# где:
# FILEPATH - путь к файлу информации о барах в формате JSON
# LONGTITUDE - долгота текущего местоположения
# LATITUDE - широта текущего мастоположения
```
## Вывод в консоль

```bash
Самый большой бар с посадочныими местами('Спорт бар «Красная машина»', 450)
Самый маленикий бар с посадочныими местами('Бар в Деловом центре Яуза', 0)
Ближайший бар от тебя c координатами :('Staropramen', [37.750290923482424, 55.61870614052117])
```

## Запуск на Windows:
происходит аналогично примеру запруска на Linux.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)