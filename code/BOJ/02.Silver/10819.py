import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
answer = -int(1e9)

for case in permutations(arr, N):
    k = 0
    for i in range(1, N):
        k += abs(case[i - 1] - case[i])
    answer = max(answer, k)
print(answer)
