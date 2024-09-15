table = [False for _ in range(10001)]
for i in range(1, 10001):
    x = i + sum(map(int, list(str(i))))
    if x < 10001:
        table[x] = True

for i in range(1, len(table)):
    if not table[i]:
        print(i)
