import sys

N, M = map(int, sys.stdin.readline().split())
_input = sys.stdin.readline().strip()
if _input == "0":
    cnt = 0
    truths = set()
else:
    cnt, *truths = map(int, _input.split())
    truths = set(truths)

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
    if px in truths:
        p[py] = px
    else:
        p[px] = py


parties = []
for _ in range(M):
    k, *men = list(map(int, sys.stdin.readline().strip().split()))
    parties.append(men)

for men in parties:
    size = len(men)
    for i in range(size - 1):
        for j in range(i + 1, size):
            union(men[i], men[j])

answer = 0
for men in parties:
    ok = True
    for man in men:
        v = find(man)
        if v in truths:
            ok = False
            break
    if ok:
        answer += 1

print(answer)
