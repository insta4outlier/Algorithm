# [2xn 타일문제](https://school.programmers.co.kr/learn/courses/30/lessons/12900)

## 코드
```python
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    x1 = 1
    x2 = 2
    nx = 0
    for i in range(n-2):
        nx = x1 + x2
        x1 = x2
        x2 = nx

    return nx % 1000000007


if __name__ == '__main__':
    answer = solution(60000)
    print(answer)

```