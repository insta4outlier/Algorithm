def solution(mats, park):
    answer = 0
    def check(sy, sx, k):
        if sy + k > len(park) or sx + k > len(park[0]):
            return False
        for y in range(sy, sy + k):
            for x in range(sx, sx + k):
                if park[y][x] != "-1":
                    return False
        return True

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                for m in mats:
                    if check(i, j, m):
                        answer = max(answer, m)

    if answer == 0:
        return -1
    return answer