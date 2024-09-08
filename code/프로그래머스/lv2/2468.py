import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    arr.append(line)

answer = 0
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

for i in range(101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    cnt = 0
    for sy in range(N):
        for sx in range(N):
            if arr[sy][sx] > i and not visited[sy][sx]:
                cnt += 1
                visited[sy][sx] = True
                q.append((sy, sx))
                while q:
                    y, x = q.popleft()
                    for dy, dx in d:
                        ny = y + dy
                        nx = x + dx
                        if -1 < ny < N and -1 < nx < N:
                            if not visited[ny][nx]:
                                visited[ny][nx] = True
                                if arr[ny][nx] > i:
                                    q.append((ny, nx))

    answer = max(cnt, answer)

print(answer)
