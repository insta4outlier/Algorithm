def solution(n, a, b):
    answer = 0
    if a > b:
        a, b = b, a
    while True:
        if a + 1 == b and (a % 2 == 1 and b % 2 == 0):
            answer += 1
            break
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        answer += 1

    return answer
