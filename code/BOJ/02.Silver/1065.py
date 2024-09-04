import sys

N = int(sys.stdin.readline().strip())
answer = 0
for i in range(1, N + 1):
    ok = True
    x = str(i)
    arr = list(map(int, list(x)))
    if len(arr) <= 2:
        answer += 1
        continue

    diff = arr[1] - arr[0]
    for j in range(2, len(arr)):
        gap = arr[j] - arr[j - 1]
        if gap != diff:
            ok = False
            break

    if ok:
        answer += 1

print(answer)
