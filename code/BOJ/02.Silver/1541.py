import sys
import re

exp = sys.stdin.readline().strip()
nums = re.findall(r'-?\d+', exp)
answer = int(nums[0])
stack = []

for i in range(1, len(nums)):
    num = int(nums[i])
    if num >= 0:
        if stack:
            x = stack.pop() - num
            stack.append(x)
        else:
            answer += num
    else:
        stack.append(num)

k = 0
if stack:
    k = sum(stack)

print(answer + k)