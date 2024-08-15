import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
arr = []
INF = int(1e9)
fires = []
jihun = []
for i in range(R):
    line = list(sys.stdin.readline().strip())
    arr.append(line)
    for j in range(C):
        if line[j] == "F":
            fires.append((i, j))
        if line[j] == "J":
            jihun.append((i, j))


def bfs(starts, fire_table):
    visited = [[False for _ in range(C)] for _ in range(R)]
    table = [[INF for _ in range(C)] for _ in range(R)]
    q = deque()
    for sy, sx in starts:
        q.append((sy, sx))
        table[sy][sx] = 0
        visited[sy][sx] = True
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if -1 < ny < R and -1 < nx < C:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if fire_table is None:
                        if arr[ny][nx] == ".":
                            table[ny][nx] = table[y][x] + 1
                            q.append((ny, nx))
                    elif table[y][x] + 1 < fire_table[ny][nx]:
                        if arr[ny][nx] == ".":
                            table[ny][nx] = table[y][x] + 1
                            q.append((ny, nx))
    return table


if not fires:
    fire_table = [[INF for _ in range(C)] for _ in range(R)]
else:
    fire_table = bfs(fires, None)

person_table = bfs(jihun, fire_table)
answer = INF

for i in range(R):
    answer = min([answer, person_table[i][0], person_table[i][-1]])

for i in range(C):
    answer = min([answer, person_table[0][i], person_table[-1][i]])

if answer == INF:
    print("IMPOSSIBLE")

else:
    print(answer + 1)
