# 2022/10/12
# 조합

import math

x,y = map(int, input().split())
cal = math.factorial(x)//(math.factorial(y)*math.factorial(x-y))
print(cal)