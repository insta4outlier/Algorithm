import sys

N = int(sys.stdin.readline().strip())
cnt = 0
for _ in range(N):
    string = sys.stdin.readline().strip()
    prev = ''
    tmp = []
    ok = True
    for ch in string:
        if not prev:
            prev = ch
        elif ch == prev:
            pass
        elif ch != prev:
            if ch in tmp:
                ok = False
                break
        tmp.append(ch)
        prev = ch
    if ok:
        cnt += 1
print(cnt)


print('hello world')