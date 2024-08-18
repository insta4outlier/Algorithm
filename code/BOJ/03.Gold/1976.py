import sys

sys.setrecursionlimit(int(1e4))
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    arr.append(line)

path = list(map(int, sys.stdin.readline().split()))
p = [-1 for _ in range(N + 1)]


def find(x):
    if p[x] == -1:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return
    p[px] = py


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union(i + 1, j + 1)

ok = True
s = set()
for k in path:
    s.add(find(k))

if len(s) == 1:
    print("YES")
else:
    print("NO")
