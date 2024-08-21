import sys

sys.setrecursionlimit(int(1e5))

N, M, K = map(int, sys.stdin.readline().split())
costs = list(map(int, sys.stdin.readline().split()))
arr = [-1 for _ in range(N)]


def find(x):
    if arr[x] <= -1:
        return x
    arr[x] = find(arr[x])
    return arr[x]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return
    arr[px] = py


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    union(a, b)

for i in range(N):
    find(i)

d = {}
for i, num in enumerate(arr):
    if num == -1:
        d[i] = []

for i, num in enumerate(arr):
    if num == -1:
        continue
    d[num].append(i)

cnt = 0
total = 0
for k, v in d.items():
    cnt += len(v) + 1
    total += min([costs[num] for num in v] + [costs[k]])

if cnt != N or total > K:
    print("Oh no")
else:
    print(total)
