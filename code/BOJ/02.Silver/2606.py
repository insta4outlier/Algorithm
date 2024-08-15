import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
arr = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

q = deque()
q.append(1)
visited[1] = True

while q:
    x = q.popleft()
    for nx in arr[x]:
        if not visited[nx]:
            visited[nx] = True
            q.append(nx)

print(visited.count(True) - 1)

