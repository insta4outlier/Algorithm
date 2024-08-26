import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
arr = []
visited = [[False for _ in range(C)] for _ in range(R)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
s = 0
w = 0

for i in range(R):
    line = list(sys.stdin.readline().strip())
    arr.append(line)

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            visited[i][j] = True
            if arr[i][j] != "#":
                q = deque()
                q.append((i, j))
                s_cnt = 0
                w_cnt = 0
                while q:
                    y, x = q.popleft()
                    if arr[y][x] == "o":
                        s_cnt += 1
                    elif arr[y][x] == "v":
                        w_cnt += 1

                    for dy, dx in d:
                        ny = y + dy
                        nx = x + dx
                        if -1 < ny < R and -1 < nx < C:
                            if not visited[ny][nx]:
                                visited[ny][nx] = True
                                if arr[ny][nx] != "#":
                                    q.append((ny, nx))

                if s_cnt > w_cnt:
                    s += s_cnt
                else:
                    w += w_cnt

print(s, w)
