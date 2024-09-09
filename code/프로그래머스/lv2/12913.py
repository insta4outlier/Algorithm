def solution(land):
    table = [x for x in land[0]]
    for i in range(1, len(land)):
        tmp = [num for num in table]
        for j in range(4):
            x = land[i][j]
            for k, num in enumerate(table):
                if j != k:
                    x = max(x, num + land[i][j])
            tmp[j] = x
        table = [num for num in tmp]
    return max(table)
