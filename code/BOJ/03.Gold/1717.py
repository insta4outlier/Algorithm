import sys
sys.setrecursionlimit(int(1e5))


n, m = map(int, sys.stdin.readline().split())
arr = [-1] * (n+1)


def find(x):
    if arr[x] == -1:
        return x
    arr[x] = find(arr[x])
    return arr[x]


def merge(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return
    arr[py] = px


for _ in range(m):
    cmd, a, b = map(int, sys.stdin.readline().split())
    if cmd == 0:
        merge(a, b)
    else:
        pa = find(a)
        pb = find(b)
        if pa == pb:
            print("YES")
        else:
            print("NO")
