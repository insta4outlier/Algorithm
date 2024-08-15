import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

q = deque()
visited = set()

q.append((A, 1))
visited.add(A)
answer = -1

while q:
    x, cnt = q.popleft()
    if x == B:
        answer = cnt
        break

    nx = x * 2
    if nx <= B:
        if nx not in visited:
            visited.add(nx)
            q.append((nx, cnt + 1))

    nx = int(str(x) + '1')
    if nx <= B:
        if nx not in visited:
            visited.add(nx)
            q.append((nx, cnt + 1))

print(answer)
