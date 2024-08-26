import sys
from collections import deque

d = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

while True:
    w, h = map(int, sys.stdin.readline().strip().split())
    if (h, w) == (0, 0):
        break
    arr = []
    visited = [[False for _ in range(w)] for _ in range(h)]
    for _ in range(h):
        line = list(map(int, sys.stdin.readline().split()))
        arr.append(line)

    answer = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                visited[i][j] = True
                if arr[i][j] == 1:
                    answer += 1
                    q = deque()
                    q.append((i, j))
                    visited[i][j] = True
                    while q:
                        y, x = q.popleft()
                        for dy, dx in d:
                            ny = y + dy
                            nx = x + dx
                            if -1 < ny < h and -1 < nx < w:
                                if not visited[ny][nx]:
                                    visited[ny][nx] = True
                                    if arr[ny][nx] == 1:
                                        q.append((ny, nx))

    print(answer)

