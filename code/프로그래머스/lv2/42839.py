from itertools import permutations

def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    cnt = len(numbers)
    numbers = list(numbers)
    check = set()
    for i in range(1, cnt + 1):
        for case in permutations(numbers, i):
            num = int(''.join(case))
            if prime(num) and num not in check:
                check.add(num)
                answer += 1

    return answer