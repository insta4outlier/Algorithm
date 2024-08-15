import sys
from collections import deque

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    _list = list(map(int, list(sys.stdin.readline().strip())))
    arr.append(_list)

d = ((0, 1), (0, -1), (1, 0), (-1, 0))
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0
cluster = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            if arr[i][j] == 1:
                cnt += 1
                k = 1
                q = deque()
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    for dy, dx in d:
                        ny = y + dy
                        nx = x + dx
                        if -1 < ny < n and -1 < nx < n:
                            if not visited[ny][nx]:
                                visited[ny][nx] = True
                                if arr[ny][nx] == 1:
                                    q.append((ny, nx))
                                    k += 1
                cluster.append(k)

cluster.sort()
print(cnt)
for item in cluster:
    print(item)
