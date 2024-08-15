import sys

sys.setrecursionlimit(int(1e5))

N = int(sys.stdin.readline().strip())
INF = int(1e9)
table = [INF for _ in range(N + 1)]
if N >= 3:
    table[3] = 1
if N >= 5:
    table[5] = 1


def dp(x):
    if x <= 5:
        return table[x]
    if table[x] != INF:
        return table[x]
    table[x] = min(table[x], dp(x - 3) + 1, dp(x - 5) + 1)
    return table[x]


ret = dp(N)
if ret == INF:
    print(-1)
else:
    print(ret)