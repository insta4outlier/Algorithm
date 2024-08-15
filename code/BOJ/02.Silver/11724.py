import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = True
        q = deque()
        q.append(i)
        cnt += 1
        while q:
            x = q.popleft()
            for nx in arr[x]:
                if not visited[nx]:
                    visited[nx] = True
                    q.append(nx)


print(cnt)
