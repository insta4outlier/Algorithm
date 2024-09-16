def solution(storey):
    arr = list(map(int, list(str(storey))))[::-1]
    size = len(arr)
    flag = False
    answer = 0
    if arr[0] <= 5:
        answer += arr[0]
    else:
        answer += 10 - arr[0]
        flag = True

    if len(arr) == 1:
        return answer if not flag else answer + 1

    for i in range(1, size):
        x = arr[i]
        if flag:
            x += 1
        elif arr[i - 1] == 5:
            if x >= 5:
                x += 1
        if x <= 5:
            answer += x
            flag = False
        else:
            answer += 10 - x
            flag = True
    if flag:
        answer += 1

    return answer