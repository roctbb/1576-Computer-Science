# Соревнования ботов

## Структура бота

Бот представляет собой программу на языке Python 3.

Файл с кодом должен содержать функцию **make_choice** принимающую ровно три аргумента.

Перед каждым ходом тестирующая система передаст в функцию три параметра - координаты бота на карте (x,y) и матрицу с информацией о других игроках.

В итоге функция должна вернуть в точку вызова строку - решение, что делать боту в **текущем** ходе.

```python
def make_choice(x,y,field):
    #произвольный код
```

## Возвращаемые значения

При каждом запуске функция должна выбрать одно из восьми действий - передвижение на одну клетку в одну из четырех сторон, либо стрельба в одном из четырех направлений.

Для этого функция make_choice должна вернуть одну из следующих строк: **"fire_up", "fire_down", "fire_left", "fire_right", "go_up","go_down","go_left","go_right"**.

Выстрел поражает только одного противника, но на произвольном расстоянии.

```python

import random

def make_choice(x,y,field):
    actions = ["fire_up", "fire_down",
               "fire_left", "fire_right", 
               "go_up","go_down",
               "go_left","go_right"]
    return random.choice(actions)
```

## Принимаемые параметры

Функция make_choice принимает три параметра - координаты танка по осям x и y, а также матрицу игры.

Матрица игры содержит информацию о:
  - Расположении игроков, монеток и стен на карте.
  - Текущем уровне жизни всех игроков.
  - Истории ходов каждого игрока с начала игры.

Физически матрица представляет собой список списков (матрицу), в которых содержится либо ноль в клетках которой может быть:
  - **0**, если клетка пустая;
  - **1**, если в клетке монетка;
  - **-1**, если в клетке стена;
  - **словарь из трех элементов**, если в клетке бот (очки здоровья бота ('life') стоящего в этой клетке, история его ходов ('history') и его имя ('name')).

  - **Как узнать, сколько жизни осталось у собственного бота?**
  - field[x][y]['life']

История ходов - список ранее отданных команд, т.е. строк вида "go_right".
  - **Как узнать, какие команды были отданы нашим ботом ранее?**
  - field[x][y]['history']

Первая координата в матрице - это значение по оси X, а вторая по оси Y. Левый верхний угол карты - это точка field[0][0]. Правый нижний угол карты - это точка field[x_size][y_size], где x_size = len(field), y_size = len(field[0]).
