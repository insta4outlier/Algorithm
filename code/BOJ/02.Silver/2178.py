import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    line = list(map(int, list(sys.stdin.readline().strip())))
    arr.append(line)

d = ((0, 1), (0, -1), (1, 0), (-1, 0))
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 1))
visited[0][0] = True

while q:
    y, x, cnt = q.popleft()
    if (y, x) == (n - 1, m - 1):
        print(cnt)
        break
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if -1 < nx < m and -1 < ny < n:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if arr[ny][nx] == 1:
                    q.append((ny, nx, cnt + 1))

