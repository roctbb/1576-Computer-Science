from copy import deepcopy

def printMap(m):
    width = len(m)
    height = len(m[0])
    for i in range(width):
        for j in range(height):
            print(m[j][i], end='')
        print('')
    print('')

mapOfCoins = [
    ['.', '.', '#', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', '*', '#', '@', '.', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.'],
]

startX = 2
startY = 3

width = len(mapOfCoins)
height = len(mapOfCoins[0])

visitedMap = deepcopy(mapOfCoins)
path = []

points = [(startX, startY, 0, path)]

while len(points) != 0:
    # ищем самую близкую точку из доступных
    points = sorted(points, key=lambda x: x[2])
    x, y, S, path = points[0]
    del points[0]

    # если точка за пределами поля
    if x < 0 or y < 0 or x >= width or y >= height:
        continue

    # если мы уже были в точке
    if visitedMap[x][y] == 'x':
        continue

    # если это стена
    if visitedMap[x][y] == '#':
        continue

    # если нашли монетку
    if mapOfCoins[x][y] == '*':
        print("path to star = ", S)
        print(path)
        printMap(mapOfCoins)
        exit()

    # помечаем клетку, как посещенную
    visitedMap[x][y] = 'x'
    # добавляем соседей в очередь
    newPath = deepcopy(path)
    newPath.append('>')
    points.append((x+1, y, S+1, newPath))

    newPath = deepcopy(path)
    newPath.append('d')
    points.append((x, y+1, S+1, newPath))

    newPath = deepcopy(path)
    newPath.append('<')
    points.append((x-1, y, S+1, newPath))

    newPath = deepcopy(path)
    newPath.append('^')
    points.append((x, y-1, S+1, newPath))

    printMap(visitedMap)

print("no path :(")