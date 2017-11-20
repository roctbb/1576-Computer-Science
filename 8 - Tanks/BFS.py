from copy import deepcopy

mapOfCoins = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', '*', '#', '@', '.', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

startX = 2
startY = 3

width = len(mapOfCoins)
height = len(mapOfCoins[0])

visitedMap = deepcopy(mapOfCoins)

points = [(startX, startY, 0)]

while len(points) != 0:
    # ищем самую близкую точку из доступных
    points = sorted(points, key=lambda x: x[2])
    x, y, S = points[0]
    del points[0]

    # если точка за пределами поля
    if x < 0 or y < 0 or x >= width or y >= height:
        continue

    # если мы уже были в точке
    if visitedMap[x][y] == 'x':
        continue

    # если нашли монетку
    if mapOfCoins[x][y] == '*':
        print("path to star = ", S)
        exit()

    # помечаем клетку, как посещенную
    visitedMap[x][y] = 'x'
    # добавляем соседей в очередь
    points.append((x+1, y, S+1))
    points.append((x, y+1, S+1))
    points.append((x-1, y, S+1))
    points.append((x, y-1, S+1))

print("no path :(")