# 2022/10/11
# 다리놓기

import math
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    case = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
    print(case)

# #시간초과
# from itertools import combinations

# T = int(input())
# for i in range(T):
#     x,y = map(int,input().split())
#     case = len(list(combinations(range(y),x)))
#     print(case)