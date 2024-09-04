from itertools import permutations

N = int(input().strip())

cases = list(permutations([x for x in range(1, N + 1)], N))
for case in cases:
    print(*case)

