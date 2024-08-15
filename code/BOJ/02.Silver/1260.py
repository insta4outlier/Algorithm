import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n + 1):
    arr[i].sort()

q = deque()

bfs_track = []
q.append(v)
visited[v] = True

while q:
    x = q.popleft()
    bfs_track.append(x)
    for nx in arr[x]:
        if not visited[nx]:
            visited[nx] = True
            q.append(nx)


stack = deque()
visited = [False for _ in range(n + 1)]
dfs_track = []
stack.append(v)
visited[v] = True

while stack:
    x = stack.pop()
    visited[x] = True
    dfs_track.append(x)
    for nx in reversed(arr[x]):
        if not visited[nx]:
            if nx not in stack:
                stack.append(nx)

print(*dfs_track)
print(*bfs_track)
