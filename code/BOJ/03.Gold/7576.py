import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
arr = []
visited = [[False for _ in range(M)] for _ in range(N)]
table = [[0 for _ in range(M)] for _ in range(N)]
q = deque()
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
cnt = 0

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if line[j] == 1:
            q.append((i, j))
            visited[i][j] = True
        elif line[j] == 0:
            cnt += 1
    arr.append(line)

while q:
    y, x = q.popleft()
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if -1 < ny < N and -1 < nx < M:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if arr[ny][nx] == 0:
                    table[ny][nx] = table[y][x] + 1
                    q.append((ny, nx))
                    cnt -= 1

if cnt != 0:
    print(-1)
else:
    answer = 0
    for i in range(N):
        for j in range(M):
            answer = max(table[i][j], answer)
    print(answer)
