# 2023/02/01
# 팩토리얼 0의 개수

import math
n = int(input())

result = 0
fac = math.factorial(n)
while(True):
    if fac % 10==0:
        result += 1
        fac = fac //10
    else:
        break

print(result)