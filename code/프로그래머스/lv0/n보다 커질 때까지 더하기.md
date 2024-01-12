# [n보다 커질 때까지 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/181884)

## 코드
```python
def solution(numbers, n):
    answer = 0
    for num in numbers:
        answer += num
        if answer > n:
            return answer
    return answer
```