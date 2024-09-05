def solution(prices):
    answer = [0 for _ in range(len(prices))]
    s = []
    for i, p in enumerate(prices):
        if not s:
            s.append((i, p))
        else:
            while s:
                if s[-1][1] > p:
                    x, _ = s.pop()
                    answer[x] = i - x
                else:
                    break
            s.append((i, p))

    if len(s) == 1:
        x, _  = s.pop()
        answer[x] = 0
    elif len(s) > 1:
        i, _ = s.pop()
        while s:
            x, _ = s.pop()
            answer[x] = i - x

    return answer