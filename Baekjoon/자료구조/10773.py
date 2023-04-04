# 2023/04/04
# 제로

import sys
k = int(sys.stdin.readline().rstrip())

stack = []
for i in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num==0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))