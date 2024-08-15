import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    line = list(sys.stdin.readline().strip())
    arr.append(line)


def bfs(visible):
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    q = deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    for dy, dx in d:
                        ny = y + dy
                        nx = x + dx
                        if -1 < nx < N and -1 < ny < N:
                            if arr[ny][nx] == arr[i][j]:
                                if not visited[ny][nx]:
                                    visited[ny][nx] = True
                                    q.append((ny, nx))
                            elif not visible and "B" not in (arr[ny][nx], arr[i][j]):
                                if not visited[ny][nx]:
                                    visited[ny][nx] = True
                                    q.append((ny, nx))
    return cnt


answer = [bfs(True), bfs(False)]
print(*answer)


