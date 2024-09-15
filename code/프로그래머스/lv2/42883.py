def solution(number, k):
    stack = []
    for string in number:
        while k and (stack and int(stack[-1]) < int(string)):
            stack.pop()
            k -= 1
        stack.append(string)

    while k:
        stack.pop()
        k -= 1

    return ''.join(stack)