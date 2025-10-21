from random import randrange

N, M = 4, 6
field = [[randrange(2) for _ in range(M)] for _ in range(N)]

visited = set()
islands = [] #размеры островов

#рекурсивная функция search для нахождения островов
def search(x, y):
    if not ((0 <= x < N) and (0 <= y < M)) or field[x][y] != 1 or (x,y) in visited:
        return 0
    visited.add((x,y))
    return 1 + search(x+1, y) + search(x-1, y) + search(x, y+1) + search(x, y-1)

for i in range(N):
    for j in range(M):
        if field[i][j] == 1 and (i,j) not in visited:
            islands.append(search(i,j))

#подсчет строк и столбцов с более чем 3 единицами
rows = sum(sum(row) > 3 for row in field)
cols = sum(sum(col) > 3 for col in zip(*field)) #для транспонированной


print("Матрица:")
for row in field:
    print(' '.join(map(str,row)))

print("Размеры островов:", islands)
print("Кол-во строк с более чем 3 единицами:", rows)
print("Кол-во столбцов с более чем 3 единицами:", cols)
